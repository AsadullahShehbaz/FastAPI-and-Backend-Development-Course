import axios from "axios"
import { ArrowLeft, PackageCheck, Truck } from "lucide-react"
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { useContext, useEffect, useState, type FormEvent } from "react"
import { Link, Navigate, useSearchParams } from "react-router"

import { ProductStatus, type ProductRead, type ProductUpdate } from "~/api/client"
import { AppSidebar } from "~/components/app-sidebar"
import { Button, buttonVariants } from "~/components/ui/button"
import { Field, FieldLabel } from "~/components/ui/field"
import { Input } from "~/components/ui/input"
import Loading from "~/components/ui/loading"
import { Separator } from "~/components/ui/separator"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "~/components/ui/sidebar"
import { AuthContext } from "~/context/auth-context"
import api from "~/lib/api"

export default function UpdateProductPage() {
  const { token, user } = useContext(AuthContext)
  const [searchParams, setSearchParams] = useSearchParams()
  const queryClient = useQueryClient()
  const rawProductId = searchParams.get("id")
  const productId = rawProductId?.trim() ?? ""
  const hasProductId = productId.length > 0
  const isValidId = hasProductId && isValidProductId(productId)

  const productQuery = useQuery({
    queryKey: ["product", productId],
    queryFn: async () => {
      if (!isValidProductId(productId)) {
        throw new Error("A valid product ID is required")
      }

      const { data } = await api.product.getProduct(productId)
      return data
    },
    enabled: Boolean(token && user === "partner" && isValidId),
  })

  const updateProduct = useMutation({
    mutationFn: async ({
      id,
      payload,
    }: {
      id: string
      payload: ProductUpdate
    }) => {
      const { data } = await api.product.patchProduct({ id }, payload)
      return data
    },
    onSuccess: async (product) => {
      await Promise.all([
        queryClient.invalidateQueries({
          queryKey: ["product", product.id],
        }),
        queryClient.invalidateQueries({ queryKey: ["products"] }),
      ])
    },
  })

  const [productIdError, setProductIdError] = useState<string | null>(null)

  if (!token || user !== "partner") {
    return <Navigate to="/" replace />
  }

  function handleProductLookup(value: string) {
    const newProductId = value.trim()

    if (!isValidProductId(newProductId)) {
      setProductIdError("Enter a valid product ID.")
      return
    }

    setProductIdError(null)
    if (newProductId === productId && productQuery.isError) {
      void productQuery.refetch()
      return
    }

    setSearchParams({ id: newProductId })
  }

  function handleProductUpdate(payload: ProductUpdate) {
    if (!isValidId) {
      return
    }

    updateProduct.reset()
    updateProduct.mutate({ id: productId, payload })
  }

  let pageContent

  if (!hasProductId || !isValidId) {
    pageContent = (
      <ProductLookupForm
        key={rawProductId ?? "no-product"}
        initialProductId={rawProductId ?? ""}
        error={
          productIdError ??
          (hasProductId ? "The product ID in the URL is invalid." : null)
        }
        onSubmit={handleProductLookup}
        onChange={() => setProductIdError("")}
      />
    )
  } else if (productQuery.isPending) {
    pageContent = (
      <div
        className="rounded-3xl border border-slate-200 bg-white p-8"
        role="status"
      >
        <Loading />
        <p className="text-center text-sm text-slate-500">
          Loading product details...
        </p>
      </div>
    )
  } else if (productQuery.isError) {
    pageContent = (
      <ProductLookupForm
        key={rawProductId ?? "no-product"}
        initialProductId={productId}
        error={getProductErrorMessage(productQuery.error)}
        onSubmit={handleProductLookup}
        onChange={() => setProductIdError("")}
      />
    )
  } else {
    pageContent = (
      <UpdateProductForm
        product={productQuery.data}
        isPending={updateProduct.isPending}
        error={
          updateProduct.isError
            ? getUpdateErrorMessage(updateProduct.error)
            : null
        }
        success={updateProduct.isSuccess ? "Product updated successfully." : null}
        onSubmit={handleProductUpdate}
      />
    )
  }

  return (
    <SidebarProvider
      style={
        {
          "--sidebar-width": "19rem",
        } as React.CSSProperties
      }
    >
      <AppSidebar currentRoute="Update product" />
      <SidebarInset className="bg-[#f7f8f5]">
        <header className="flex h-16 shrink-0 items-center gap-2 border-b border-slate-200/80 bg-white/80 px-4 sm:px-6">
          <SidebarTrigger className="-ml-1" />
          <Separator
            orientation="vertical"
            className="mr-2 data-[orientation=vertical]:h-4"
          />
          <h1 className="text-sm font-semibold">Update product</h1>
        </header>

        <main className="mx-auto w-full max-w-7xl flex-1 p-5 sm:p-8">
          <div className="mb-8">
            <Link
              to="/dashboard"
              className={buttonVariants({
                variant: "ghost",
                className: "mb-4 -ml-3 text-slate-600",
              })}
            >
              <ArrowLeft aria-hidden="true" />
              Back to dashboard
            </Link>
            <p className="text-sm font-medium text-emerald-800">
              Delivery partner workspace
            </p>
            <h2 className="mt-2 text-3xl font-semibold tracking-tight sm:text-4xl">
              Keep a delivery moving.
            </h2>
            <p className="mt-3 max-w-2xl leading-6 text-slate-600">
              Find a product by its ID, then update its status and delivery
              details.
            </p>
          </div>

          {pageContent}
        </main>
      </SidebarInset>
    </SidebarProvider>
  )
}

function ProductLookupForm({
  initialProductId,
  error,
  onSubmit,
  onChange,
}: {
  initialProductId: string
  error: string | null
  onSubmit: (productId: string) => void
  onChange: () => void
}) {
  const [productId, setProductId] = useState(initialProductId)

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    onSubmit(productId)
  }

  return (
    <section className="max-w-2xl rounded-3xl border border-slate-200 bg-white p-5 shadow-sm sm:p-8">
      <span className="flex size-12 items-center justify-center rounded-2xl bg-emerald-50 text-emerald-800">
        <Truck className="size-6" aria-hidden="true" />
      </span>
      <h3 className="mt-5 text-xl font-semibold">Find a product to update</h3>
      <p className="mt-2 leading-6 text-slate-600">
        Enter the product UUID from the dashboard, then load its delivery
        details.
      </p>

      <form className="mt-6 space-y-4" onSubmit={handleSubmit}>
        <Field>
          <FieldLabel htmlFor="product-id">Product ID</FieldLabel>
          <Input
            id="product-id"
            name="product-id"
            value={productId}
            onChange={(event) => {
              setProductId(event.currentTarget.value)
              onChange()
            }}
            placeholder="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
            required
          />
        </Field>
        {error && (
          <p
            className="rounded-xl bg-rose-50 px-4 py-3 text-sm text-rose-800"
            role="alert"
          >
            {error}
          </p>
        )}
        <Button type="submit" className="rounded-full px-5">
          Load product
        </Button>
      </form>
    </section>
  )
}

function UpdateProductForm({
  product,
  isPending,
  error,
  success,
  onSubmit,
}: {
  product: ProductRead
  isPending: boolean
  error: string | null
  success: string | null
  onSubmit: (payload: ProductUpdate) => void
}) {
  const [status, setStatus] = useState(product.status)
  const [location, setLocation] = useState(getCurrentLocation(product))
  const [description, setDescription] = useState(getCurrentDescription(product))
  const [estimatedDelivery, setEstimatedDelivery] = useState(
    toDateTimeLocal(product.estimated_delivery)
  )
  const [formError, setFormError] = useState<string | null>(null)

  useEffect(() => {
    setStatus(product.status)
    setLocation(getCurrentLocation(product))
    setDescription(getCurrentDescription(product))
    setEstimatedDelivery(toDateTimeLocal(product.estimated_delivery))
    setFormError(null)
  }, [product])

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setFormError(null)

    const update: ProductUpdate = {}
    const currentLocation = getCurrentLocation(product)
    const currentDescription = getCurrentDescription(product)

    if (status !== product.status) {
      update.status = status
    }

    if (location.trim()) {
      const locationNumber = Number(location)

      if (!Number.isSafeInteger(locationNumber) || locationNumber < 0) {
        setFormError("Enter a valid ZIP code for the current location.")
        return
      }

      if (!currentLocation || locationNumber !== Number(currentLocation)) {
        update.location = locationNumber
      }
    }

    if (
      description.trim() &&
      description.trim() !== currentDescription.trim()
    ) {
      update.description = description.trim()
    }

    if (estimatedDelivery) {
      const newDeliveryDate = new Date(estimatedDelivery)

      if (Number.isNaN(newDeliveryDate.getTime())) {
        setFormError("Enter a valid estimated delivery date.")
        return
      }

      const currentDeliveryDate = new Date(product.estimated_delivery)
      if (
        Number.isNaN(currentDeliveryDate.getTime()) ||
        newDeliveryDate.getTime() !== currentDeliveryDate.getTime()
      ) {
        update.estimated_delivery = newDeliveryDate.toISOString()
      }
    }

    if (Object.keys(update).length === 0) {
      setFormError("Make at least one change before submitting.")
      return
    }

    onSubmit(update)
  }

  return (
    <section className="grid items-start gap-6 lg:grid-cols-[minmax(0,1fr)_300px]">
      <div className="rounded-3xl border border-slate-200 bg-white p-5 shadow-sm sm:p-8">
        <div className="mb-7 flex items-center gap-3">
          <span className="flex size-11 items-center justify-center rounded-xl bg-emerald-50 text-emerald-800">
            <PackageCheck className="size-5" aria-hidden="true" />
          </span>
          <div className="min-w-0">
            <h3 className="font-semibold">{product.name}</h3>
            <p className="truncate text-sm text-slate-500">{product.id}</p>
          </div>
        </div>

        <form className="space-y-5" onSubmit={handleSubmit}>
          <Field>
            <FieldLabel htmlFor="status">Delivery status</FieldLabel>
            <select
              id="status"
              name="status"
              value={status}
              onChange={(event) => {
                if (isProductStatus(event.currentTarget.value)) {
                  setStatus(event.currentTarget.value)
                }
              }}
              className="h-10 w-full rounded-lg border border-input bg-white px-3 text-sm capitalize outline-none focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50"
            >
              {Object.values(ProductStatus).map((productStatus) => (
                <option key={productStatus} value={productStatus}>
                  {productStatus.replaceAll("_", " ")}
                </option>
              ))}
            </select>
          </Field>

          <Field>
            <FieldLabel htmlFor="location">Current location ZIP code</FieldLabel>
            <Input
              id="location"
              name="location"
              type="number"
              min="0"
              step="1"
              value={location}
              onChange={(event) => setLocation(event.currentTarget.value)}
              placeholder="94105"
            />
          </Field>

          <Field>
            <FieldLabel htmlFor="description">Delivery note</FieldLabel>
            <Input
              id="description"
              name="description"
              value={description}
              onChange={(event) => setDescription(event.currentTarget.value)}
              placeholder="Add a short update for the delivery timeline"
            />
          </Field>

          <Field>
            <FieldLabel htmlFor="estimated_delivery">
              Estimated delivery
            </FieldLabel>
            <Input
              id="estimated_delivery"
              name="estimated_delivery"
              type="datetime-local"
              value={estimatedDelivery}
              onChange={(event) =>
                setEstimatedDelivery(event.currentTarget.value)
              }
            />
          </Field>

          {formError && (
            <p
              className="rounded-xl bg-rose-50 px-4 py-3 text-sm text-rose-800"
              role="alert"
            >
              {formError}
            </p>
          )}
          {error && (
            <p
              className="rounded-xl bg-rose-50 px-4 py-3 text-sm text-rose-800"
              role="alert"
            >
              {error}
            </p>
          )}
          {success && (
            <p
              className="rounded-xl bg-emerald-50 px-4 py-3 text-sm text-emerald-800"
              role="status"
            >
              {success}
            </p>
          )}

          <div className="flex flex-col-reverse gap-3 border-t border-slate-100 pt-5 sm:flex-row sm:justify-end">
            <Link
              to="/dashboard"
              className={buttonVariants({
                variant: "outline",
                className: "h-10 rounded-full px-5",
              })}
            >
              Cancel
            </Link>
            <Button
              type="submit"
              disabled={isPending}
              className="h-10 rounded-full px-5"
            >
              {isPending ? "Saving..." : "Save update"}
            </Button>
          </div>
        </form>
      </div>

      <aside className="rounded-3xl bg-emerald-950 p-6 text-white">
        <h3 className="text-lg font-semibold">Product destination</h3>
        <p className="mt-2 text-sm text-emerald-100/80">
          Delivery address ZIP code
        </p>
        <p className="mt-1 text-2xl font-semibold">{product.destination}</p>
        <p className="mt-6 text-sm leading-6 text-emerald-100/80">
          Updates are added to the product timeline and shown on the dashboard.
        </p>
      </aside>
    </section>
  )
}

function getCurrentLocation(product: ProductRead) {
  const latestEvent = product.timeline[product.timeline.length - 1]
  return latestEvent ? String(latestEvent.location) : ""
}

function getCurrentDescription(product: ProductRead) {
  const latestEvent = product.timeline[product.timeline.length - 1]
  return latestEvent?.description ?? ""
}

function toDateTimeLocal(value: string) {
  const date = new Date(value)
  if (Number.isNaN(date.getTime())) {
    return ""
  }

  const localDate = new Date(date.getTime() - date.getTimezoneOffset() * 60_000)
  return localDate.toISOString().slice(0, 16)
}

function isValidProductId(value: string) {
  return /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(
    value
  )
}

function isProductStatus(value: string): value is ProductStatus {
  return Object.values(ProductStatus).some((status) => status === value)
}

function getProductErrorMessage(error: unknown) {
  if (axios.isAxiosError(error) && error.response?.status === 404) {
    return "That product could not be found. Check the ID and try again."
  }

  return "Could not load that product. Check the ID and try again."
}

function getUpdateErrorMessage(error: unknown) {
  if (axios.isAxiosError(error)) {
    if (error.response?.status === 401 || error.response?.status === 403) {
      return "You are not assigned to update this product."
    }

    if (error.response?.status === 404) {
      return "That product could not be found."
    }
  }

  return "The product could not be updated. Check your changes and try again."
}
