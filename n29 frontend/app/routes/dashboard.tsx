import { useQuery } from "@tanstack/react-query"
import {
  Boxes,
  CircleCheck,
  Clock3,
  MapPin,
  Package,
  PackageCheck,
  TriangleAlert,
} from "lucide-react"
import { useContext } from "react"
import { Link, Navigate } from "react-router"

import { ProductStatus } from "~/api/client"
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

export default function DashboardPage() {
  const { token, user } = useContext(AuthContext)

  const { isLoading, isError, data, refetch } = useQuery({
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
    enabled: Boolean(token && user),
  })

  if (!token || !user) {
    return <Navigate to="/" />
  }

  if (isError) {
    return (
      <main className="flex min-h-svh items-center justify-center bg-[#f7f8f5] p-6">
        <div className="w-full max-w-md rounded-3xl border border-slate-200 bg-white p-8 text-center shadow-sm">
          <span className="mx-auto flex size-14 items-center justify-center rounded-2xl bg-rose-50 text-rose-700">
            <TriangleAlert className="size-7" aria-hidden="true" />
          </span>
          <h1 className="mt-5 text-2xl font-semibold tracking-tight">
            We couldn&apos;t load your products
          </h1>
          <p className="mt-2 leading-6 text-slate-600">
            Please check your connection and try again.
          </p>
          <Button
            className="mt-6 rounded-full px-5"
            onClick={() => refetch()}
          >
            Try again
          </Button>
        </div>
      </main>
    )
  }

  const activeProducts =
    data?.filter(
      (product) =>
        product.status === ProductStatus.Placed ||
        product.status === ProductStatus.InTransit ||
        product.status === ProductStatus.OutForDelivery
    ).length ?? 0
  const deliveredProducts =
    data?.filter((product) => product.status === ProductStatus.Delivered)
      .length ?? 0

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
          <h1 className="text-sm font-semibold">Dashboard</h1>
          <span className="ml-auto rounded-full bg-emerald-50 px-3 py-1 text-xs font-medium text-emerald-800 capitalize">
            {user === "seller" ? "Seller workspace" : "Delivery partner"}
          </span>
        </header>

        <div className="mx-auto flex w-full max-w-7xl flex-1 flex-col gap-8 p-5 sm:p-8">
          <section className="relative overflow-hidden rounded-[2rem] bg-emerald-950 px-6 py-8 text-white sm:px-9 sm:py-10">
            <div
              className="absolute -right-10 -top-20 size-64 rounded-full bg-emerald-700/40 blur-3xl"
              aria-hidden="true"
            />
            <div className="relative flex items-center justify-between gap-6">
              <div>
                <p className="text-sm font-medium text-emerald-200">
                  Welcome back
                </p>
                <h2 className="mt-2 text-3xl font-semibold tracking-tight sm:text-4xl">
                  {user === "seller"
                    ? "Your store, at a glance."
                    : "Your deliveries, at a glance."}
                </h2>
                <p className="mt-3 max-w-xl leading-6 text-emerald-100/80">
                  {user === "seller"
                    ? "Keep track of your products and see how each order is moving."
                    : "See the products on your route and follow their delivery progress."}
                </p>
              </div>
              <span className="hidden size-16 shrink-0 items-center justify-center rounded-2xl bg-white/10 text-lime-300 sm:flex">
                <PackageCheck className="size-8" aria-hidden="true" />
              </span>
            </div>
          </section>

          {isLoading || !data ? (
            <div className="rounded-3xl border border-slate-200 bg-white p-8">
              <Loading />
            </div>
          ) : (
            <>
              <section aria-labelledby="overview-heading">
                <div className="mb-4">
                  <h2
                    id="overview-heading"
                    className="text-lg font-semibold tracking-tight"
                  >
                    Overview
                  </h2>
                  <p className="mt-1 text-sm text-slate-500">
                    A quick look at your products
                  </p>
                </div>

                <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
                  <Card className="rounded-2xl border-slate-200 bg-white shadow-sm">
                    <CardContent className="flex items-center justify-between p-5">
                      <div>
                        <p className="text-sm text-slate-500">Total products</p>
                        <p className="mt-2 text-3xl font-semibold tracking-tight">
                          {data.length}
                        </p>
                      </div>
                      <span className="flex size-12 items-center justify-center rounded-2xl bg-emerald-50 text-emerald-800">
                        <Boxes className="size-6" aria-hidden="true" />
                      </span>
                    </CardContent>
                  </Card>

                  <Card className="rounded-2xl border-slate-200 bg-white shadow-sm">
                    <CardContent className="flex items-center justify-between p-5">
                      <div>
                        <p className="text-sm text-slate-500">In progress</p>
                        <p className="mt-2 text-3xl font-semibold tracking-tight">
                          {activeProducts}
                        </p>
                      </div>
                      <span className="flex size-12 items-center justify-center rounded-2xl bg-amber-50 text-amber-800">
                        <Clock3 className="size-6" aria-hidden="true" />
                      </span>
                    </CardContent>
                  </Card>

                  <Card className="rounded-2xl border-slate-200 bg-white shadow-sm sm:col-span-2 xl:col-span-1">
                    <CardContent className="flex items-center justify-between p-5">
                      <div>
                        <p className="text-sm text-slate-500">Delivered</p>
                        <p className="mt-2 text-3xl font-semibold tracking-tight">
                          {deliveredProducts}
                        </p>
                      </div>
                      <span className="flex size-12 items-center justify-center rounded-2xl bg-blue-50 text-blue-700">
                        <CircleCheck className="size-6" aria-hidden="true" />
                      </span>
                    </CardContent>
                  </Card>
                </div>
              </section>

              <section aria-labelledby="products-heading">
                <div className="mb-4 flex items-end justify-between gap-4">
                  <div>
                    <h2
                      id="products-heading"
                      className="text-lg font-semibold tracking-tight"
                    >
                      Your products
                    </h2>
                    <p className="mt-1 text-sm text-slate-500">
                      See the latest details and delivery status
                    </p>
                  </div>
                  <span className="shrink-0 rounded-full bg-white px-3 py-1 text-sm font-medium text-slate-600 ring-1 ring-slate-200">
                    {data.length} {data.length === 1 ? "product" : "products"}
                  </span>
                </div>

                {data.length === 0 ? (
                  <div className="rounded-3xl border border-dashed border-slate-300 bg-white px-6 py-12 text-center">
                    <span className="mx-auto flex size-14 items-center justify-center rounded-2xl bg-emerald-50 text-emerald-800">
                      <Package className="size-7" aria-hidden="true" />
                    </span>
                    <h3 className="mt-4 text-lg font-semibold">
                      No products yet
                    </h3>
                    <p className="mt-2 text-sm text-slate-500">
                      Your products will appear here when they are available.
                    </p>
                  </div>
                ) : (
                  <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
                    {data.map((product) => (
                      <Card
                        key={product.id}
                        className="rounded-2xl border-slate-200 bg-white shadow-sm transition hover:-translate-y-0.5 hover:shadow-md"
                      >
                        <Link
                          to={`/products/${encodeURIComponent(product.id)}`}
                          aria-label={`View details for ${product.name}`}
                          className="flex min-w-0 flex-1 flex-col rounded-2xl outline-none focus-visible:ring-2 focus-visible:ring-emerald-700"
                        >
                          <CardHeader className="border-b border-slate-100 p-5">
                            <div className="flex items-start justify-between gap-3">
                              <div className="flex min-w-0 items-center gap-3">
                                <span className="flex size-11 shrink-0 items-center justify-center rounded-xl bg-emerald-50 text-emerald-800">
                                  <Package className="size-5" aria-hidden="true" />
                                </span>
                                <div className="min-w-0">
                                  <CardTitle className="truncate text-base font-semibold">
                                    {product.name}
                                  </CardTitle>
                                  <CardDescription className="mt-1 text-xs text-slate-500">
                                    View product details
                                  </CardDescription>
                                </div>
                              </div>
                              <span
                                className={`shrink-0 rounded-full px-2.5 py-1 text-xs font-medium capitalize ${getStatusClasses(product.status)}`}
                              >
                                {product.status.replaceAll("_", " ")}
                              </span>
                            </div>
                          </CardHeader>
                          <CardContent className="grid flex-1 grid-cols-2 gap-4 p-5">
                            <div>
                              <p className="text-xs text-slate-500">Price</p>
                              <p className="mt-1 font-semibold">
                                ${product.price.toFixed(2)}
                              </p>
                            </div>
                            <div>
                              <p className="text-xs text-slate-500">Stock</p>
                              <p className="mt-1 font-semibold">
                                {product.stock} units
                              </p>
                            </div>
                            <div className="col-span-2 flex items-center gap-2 border-t border-slate-100 pt-4 text-sm text-slate-600">
                              <MapPin
                                className="size-4 shrink-0 text-emerald-700"
                                aria-hidden="true"
                              />
                              <span>
                                Destination ZIP: {product.destination}
                              </span>
                            </div>
                          </CardContent>
                        </Link>
                        {user === "partner" && (
                          <CardContent className="pt-0">
                            <Link
                              to={`/partner/products/update?id=${encodeURIComponent(product.id)}`}
                              className={buttonVariants({
                                variant: "outline",
                                className:
                                  "h-9 w-full rounded-full border-slate-200",
                              })}
                            >
                              Update product
                            </Link>
                          </CardContent>
                        )}
                      </Card>
                    ))}
                  </div>
                )}
              </section>
            </>
          )}
        </div>
      </SidebarInset>
    </SidebarProvider>
  )
}
