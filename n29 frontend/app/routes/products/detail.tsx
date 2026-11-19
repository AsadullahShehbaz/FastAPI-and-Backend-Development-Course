import axios from "axios"
import {
  ArrowLeft,
  Boxes,
  CalendarDays,
  DollarSign,
  MapPin,
  Package,
  Tag,
  TriangleAlert,
} from "lucide-react"
import { useQuery } from "@tanstack/react-query"
import { useContext } from "react"
import { Link, Navigate, useParams } from "react-router"

import {
  ProductStatus,
  type ProductRead,
} from "~/api/client"
import { AppSidebar } from "~/components/app-sidebar"
import { Button, buttonVariants } from "~/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "~/components/ui/card"
import Loading from "~/components/ui/loading"
import { Separator } from "~/components/ui/separator"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "~/components/ui/sidebar"
import { AuthContext } from "~/context/auth-context"
import api from "~/lib/api"

export default function ProductDetailPage() {
  const { token, user } = useContext(AuthContext)
  const { id = "" } = useParams()
  const isValidId = isValidProductId(id)

  const productQuery = useQuery({
    queryKey: ["products", user],
    queryFn: async () => {
      if (!user) {
        throw new Error("An account type is required to load products")
      }

      const getProducts =
        user === "seller"
          ? api.seller.getSellerProducts
          : api.partner.getPartnerProducts
      const { data } = await getProducts()
      return data
    },
    enabled: Boolean(token && user && isValidId),
  })
  const product = productQuery.data?.find((item) => item.id === id)

  if (!token || !user) {
    return <Navigate to="/" replace />
  }

  return (
    <SidebarProvider
      style={
        {
          "--sidebar-width": "19rem",
        } as React.CSSProperties
      }
    >
      <AppSidebar currentRoute="Dashboard" />
      <SidebarInset className="bg-[#f7f8f5]">
        <header className="flex h-16 shrink-0 items-center gap-2 border-b border-slate-200/80 bg-white/80 px-4 sm:px-6">
          <SidebarTrigger className="-ml-1" />
          <Separator
            orientation="vertical"
            className="mr-2 data-[orientation=vertical]:h-4"
          />
          <h1 className="text-sm font-semibold">Product details</h1>
        </header>

        <main className="mx-auto w-full max-w-7xl flex-1 p-5 sm:p-8">
          <Link
            to="/dashboard"
            className={buttonVariants({
              variant: "ghost",
              className: "mb-5 -ml-3 text-slate-600",
            })}
          >
            <ArrowLeft aria-hidden="true" />
            Back to dashboard
          </Link>

          {!isValidId ? (
            <ProductMessage
              title="Invalid product ID"
              message="This product link is not valid. Return to the dashboard and select a product."
            />
          ) : productQuery.isPending ? (
            <div className="rounded-3xl border border-slate-200 bg-white p-8">
              <Loading />
            </div>
          ) : productQuery.isError ? (
            <ProductMessage
              title="We couldn’t load this product"
              message={getProductErrorMessage(productQuery.error)}
              action={
                <Button
                  className="mt-5 rounded-full px-5"
                  onClick={() => productQuery.refetch()}
                >
                  Try again
                </Button>
              }
            />
          ) : !product ? (
            <ProductMessage
              title="Product not found"
              message="This product is not available in your account's product list."
            />
          ) : (
            <ProductDetails product={product} user={user} />
          )}
        </main>
      </SidebarInset>
    </SidebarProvider>
  )
}

function ProductDetails({
  product,
  user,
}: {
  product: ProductRead
  user: "seller" | "partner"
}) {
  const timeline = [...product.timeline].sort(
    (first, second) =>
      new Date(first.created_at).getTime() -
      new Date(second.created_at).getTime()
  )

  return (
    <div className="space-y-8">
      <section className="relative overflow-hidden rounded-[2rem] bg-emerald-950 px-6 py-8 text-white sm:px-9 sm:py-10">
        <div className="relative flex flex-wrap items-start justify-between gap-6">
          <div className="min-w-0">
            <p className="text-sm font-medium text-emerald-200">
              Complete product history
            </p>
            <h2 className="mt-2 break-words text-3xl font-semibold tracking-tight sm:text-4xl">
              {product.name}
            </h2>
            <p className="mt-3 break-all text-sm text-emerald-100/70">
              Product ID: {product.id}
            </p>
          </div>
          <div className="flex items-center gap-3">
            <span
              className={`rounded-full px-3 py-1.5 text-sm font-medium capitalize ${getStatusClasses(product.status)}`}
            >
              {product.status.replaceAll("_", " ")}
            </span>
            {user === "partner" && (
              <Link
                to={`/partner/products/update?id=${encodeURIComponent(product.id)}`}
                className={buttonVariants({
                  variant: "secondary",
                  className: "rounded-full px-4",
                })}
              >
                Update product
              </Link>
            )}
          </div>
        </div>
      </section>

      <section aria-labelledby="product-overview-heading">
        <div className="mb-4">
          <h2
            id="product-overview-heading"
            className="text-lg font-semibold tracking-tight"
          >
            Product overview
          </h2>
          <p className="mt-1 text-sm text-slate-500">
            Key information and current delivery details
          </p>
        </div>
        <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
          <OverviewCard
            icon={<DollarSign className="size-5" aria-hidden="true" />}
            label="Price"
            value={`$${product.price.toFixed(2)}`}
          />
          <OverviewCard
            icon={<Boxes className="size-5" aria-hidden="true" />}
            label="Stock"
            value={`${product.stock} units`}
          />
          <OverviewCard
            icon={<MapPin className="size-5" aria-hidden="true" />}
            label="Destination ZIP"
            value={String(product.destination)}
          />
          <OverviewCard
            icon={<CalendarDays className="size-5" aria-hidden="true" />}
            label="Estimated delivery"
            value={formatDate(product.estimated_delivery)}
          />
        </div>
      </section>

      <div className="grid items-start gap-6 lg:grid-cols-[minmax(0,1.3fr)_minmax(280px,0.7fr)]">
        <Card className="rounded-3xl border-slate-200 bg-white shadow-sm">
          <CardHeader className="border-b border-slate-100 p-5 sm:p-6">
            <CardTitle className="text-lg font-semibold">
              Delivery timeline
            </CardTitle>
            <CardDescription>
              {timeline.length} {timeline.length === 1 ? "event" : "events"} ·
              oldest first
            </CardDescription>
          </CardHeader>
          <CardContent className="p-5 sm:p-6">
            {timeline.length === 0 ? (
              <p className="py-6 text-center text-sm text-slate-500">
                No delivery events have been recorded yet.
              </p>
            ) : (
              <ol className="space-y-0">
                {timeline.map((event, index) => (
                  <li
                    key={event.id}
                    className="relative pb-7 pl-8 last:pb-0"
                  >
                    {index < timeline.length - 1 && (
                      <span
                        className="absolute top-4 bottom-0 left-[5px] w-px bg-emerald-100"
                        aria-hidden="true"
                      />
                    )}
                    <span
                      className="absolute top-1 left-0 flex size-3 items-center justify-center rounded-full bg-emerald-600 ring-4 ring-emerald-50"
                      aria-hidden="true"
                    />
                    <div className="flex flex-wrap items-center justify-between gap-2">
                      <h3 className="font-semibold capitalize">
                        {event.status.replaceAll("_", " ")}
                      </h3>
                      <time
                        className="text-sm text-slate-500"
                        dateTime={event.created_at}
                      >
                        {formatDate(event.created_at)}
                      </time>
                    </div>
                    <p className="mt-2 flex items-center gap-2 text-sm text-slate-600">
                      <MapPin
                        className="size-4 text-emerald-700"
                        aria-hidden="true"
                      />
                      Location ZIP: {event.location}
                    </p>
                    {event.description && (
                      <p className="mt-2 text-sm leading-6 text-slate-600">
                        {event.description}
                      </p>
                    )}
                  </li>
                ))}
              </ol>
            )}
          </CardContent>
        </Card>

        <div className="space-y-6">
          <Card className="rounded-3xl border-slate-200 bg-white shadow-sm">
            <CardHeader className="border-b border-slate-100 p-5">
              <CardTitle className="text-base font-semibold">
                Seller details
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-3 p-5">
              <div>
                <p className="text-xs text-slate-500">Name</p>
                <p className="mt-1 font-medium">{product.seller.name}</p>
              </div>
              <div>
                <p className="text-xs text-slate-500">Email</p>
                <a
                  href={`mailto:${product.seller.email}`}
                  className="mt-1 inline-block break-all font-medium text-emerald-800 underline-offset-4 hover:underline"
                >
                  {product.seller.email}
                </a>
              </div>
            </CardContent>
          </Card>

          <Card className="rounded-3xl border-slate-200 bg-white shadow-sm">
            <CardHeader className="border-b border-slate-100 p-5">
              <CardTitle className="flex items-center gap-2 text-base font-semibold">
                <Tag className="size-4 text-emerald-700" aria-hidden="true" />
                Product tags
              </CardTitle>
            </CardHeader>
            <CardContent className="p-5">
              {product.tags.length === 0 ? (
                <p className="text-sm text-slate-500">
                  No tags have been added.
                </p>
              ) : (
                <ul className="space-y-3">
                  {product.tags.map((tag) => (
                    <li
                      key={tag.name}
                      className="rounded-xl bg-[#f7f8f5] p-3"
                    >
                      <p className="font-medium capitalize">
                        {tag.name.replaceAll("_", " ")}
                      </p>
                      <p className="mt-1 text-sm leading-5 text-slate-600">
                        {tag.instruction}
                      </p>
                    </li>
                  ))}
                </ul>
              )}
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}

function OverviewCard({
  icon,
  label,
  value,
}: {
  icon: React.ReactNode
  label: string
  value: string
}) {
  return (
    <Card className="rounded-2xl border-slate-200 bg-white shadow-sm">
      <CardContent className="flex items-center justify-between gap-3 p-5">
        <div className="min-w-0">
          <p className="text-sm text-slate-500">{label}</p>
          <p className="mt-2 truncate text-lg font-semibold">{value}</p>
        </div>
        <span className="flex size-11 shrink-0 items-center justify-center rounded-xl bg-emerald-50 text-emerald-800">
          {icon}
        </span>
      </CardContent>
    </Card>
  )
}

function ProductMessage({
  title,
  message,
  action,
}: {
  title: string
  message: string
  action?: React.ReactNode
}) {
  return (
    <div className="mx-auto max-w-lg rounded-3xl border border-slate-200 bg-white p-8 text-center shadow-sm">
      <span className="mx-auto flex size-14 items-center justify-center rounded-2xl bg-amber-50 text-amber-800">
        <TriangleAlert className="size-7" aria-hidden="true" />
      </span>
      <h2 className="mt-5 text-2xl font-semibold tracking-tight">{title}</h2>
      <p className="mt-2 leading-6 text-slate-600">{message}</p>
      {action}
    </div>
  )
}

function getStatusClasses(status: ProductStatus) {
  if (status === ProductStatus.Delivered) {
    return "bg-emerald-50 text-emerald-700"
  }

  if (status === ProductStatus.Cancelled) {
    return "bg-rose-50 text-rose-700"
  }

  if (status === ProductStatus.InTransit) {
    return "bg-blue-50 text-blue-700"
  }

  if (status === ProductStatus.OutForDelivery) {
    return "bg-violet-50 text-violet-700"
  }

  return "bg-amber-50 text-amber-800"
}

function formatDate(value: string) {
  const date = new Date(value)
  if (Number.isNaN(date.getTime())) {
    return "Not available"
  }

  return new Intl.DateTimeFormat("en-US", {
    dateStyle: "medium",
    timeStyle: "short",
  }).format(date)
}

function isValidProductId(value: string) {
  return /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(
    value
  )
}

function getProductErrorMessage(error: unknown) {
  if (
    axios.isAxiosError(error) &&
    (error.response?.status === 401 || error.response?.status === 403)
  ) {
    return "Your session cannot load these products. Sign in again and try."
  }

  return "Could not load product details. Please check your connection and try again."
}
