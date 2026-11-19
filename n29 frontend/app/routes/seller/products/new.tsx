import axios from "axios"
import { ArrowLeft, PackagePlus, ShieldCheck } from "lucide-react"
import { useMutation, useQueryClient } from "@tanstack/react-query"
import { useContext, useRef, useState, type FormEvent } from "react"
import { Link, Navigate } from "react-router"

import type { ProductCreate } from "~/api/client"
import { AppSidebar } from "~/components/app-sidebar"
import { Button, buttonVariants } from "~/components/ui/button"
import { Field, FieldLabel } from "~/components/ui/field"
import { Input } from "~/components/ui/input"
import { Separator } from "~/components/ui/separator"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "~/components/ui/sidebar"
import { AuthContext } from "~/context/auth-context"
import api from "~/lib/api"

export default function SubmitProductPage() {
  const { token, user } = useContext(AuthContext)
  const queryClient = useQueryClient()
  const formRef = useRef<HTMLFormElement>(null)
  const [formError, setFormError] = useState<string | null>(null)
  const [successMessage, setSuccessMessage] = useState<string | null>(null)

  const submitProduct = useMutation({
    mutationFn: async (payload: ProductCreate) => {
      const { data } = await api.product.createProduct(payload)
      return data
    },
    onSuccess: async (createdProduct) => {
      formRef.current?.reset()
      setSuccessMessage(`Product ${createdProduct.id} was submitted.`)
      await queryClient.invalidateQueries({ queryKey: ["products"] })
    },
  })

  if (!token || user !== "seller") {
    return <Navigate to="/" replace />
  }

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setFormError(null)
    setSuccessMessage(null)
    submitProduct.reset()

    const formData = new FormData(event.currentTarget)
    const name = String(formData.get("name") ?? "").trim()
    const priceValue = String(formData.get("price") ?? "").trim()
    const stockValue = String(formData.get("stock") ?? "").trim()
    const destinationValue = String(formData.get("destination") ?? "").trim()
    const clientEmail = String(
      formData.get("client_contact_email") ?? ""
    ).trim()
    const clientPhone = String(
      formData.get("client_contact_phone") ?? ""
    ).trim()

    const price = Number(priceValue)
    const stock = Number(stockValue)
    const destination = Number(destinationValue)

    if (
      name.length < 3 ||
      name.length > 100 ||
      !priceValue ||
      !Number.isFinite(price) ||
      price <= 0 ||
      !stockValue ||
      !Number.isSafeInteger(stock) ||
      stock <= 0 ||
      !destinationValue ||
      !Number.isSafeInteger(destination) ||
      destination < 0 ||
      !clientEmail
    ) {
      setFormError("Check the product details and try again.")
      return
    }

    const payload: ProductCreate = {
      name,
      price,
      stock,
      destination,
      client_contact_email: clientEmail,
      ...(clientPhone ? { client_contact_phone: clientPhone } : {}),
    }

    submitProduct.mutate(payload)
  }

  return (
    <SidebarProvider
      style={
        {
          "--sidebar-width": "19rem",
        } as React.CSSProperties
      }
    >
      <AppSidebar currentRoute="Submit product" />
      <SidebarInset className="bg-[#f7f8f5]">
        <header className="flex h-16 shrink-0 items-center gap-2 border-b border-slate-200/80 bg-white/80 px-4 sm:px-6">
          <SidebarTrigger className="-ml-1" />
          <Separator
            orientation="vertical"
            className="mr-2 data-[orientation=vertical]:h-4"
          />
          <h1 className="text-sm font-semibold">Submit a product</h1>
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
              Seller workspace
            </p>
            <h2 className="mt-2 text-3xl font-semibold tracking-tight sm:text-4xl">
              Send something on its way.
            </h2>
            <p className="mt-3 max-w-2xl leading-6 text-slate-600">
              Add the product and delivery details below. We&apos;ll find an
              available delivery partner for its destination.
            </p>
          </div>

          <div className="grid items-start gap-6 lg:grid-cols-[minmax(0,1fr)_300px]">
            <section className="rounded-3xl border border-slate-200 bg-white p-5 shadow-sm sm:p-8">
              <div className="mb-7 flex items-center gap-3">
                <span className="flex size-11 items-center justify-center rounded-xl bg-emerald-50 text-emerald-800">
                  <PackagePlus className="size-5" aria-hidden="true" />
                </span>
                <div>
                  <h3 className="font-semibold">Product details</h3>
                  <p className="text-sm text-slate-500">
                    Fields marked required must be filled in.
                  </p>
                </div>
              </div>

              <form
                ref={formRef}
                className="space-y-5"
                onSubmit={handleSubmit}
              >
                <Field>
                  <FieldLabel htmlFor="name">Product name</FieldLabel>
                  <Input
                    id="name"
                    name="name"
                    placeholder="For example, Ceramic travel mug"
                    minLength={3}
                    maxLength={100}
                    required
                  />
                </Field>

                <div className="grid gap-5 sm:grid-cols-2">
                  <Field>
                    <FieldLabel htmlFor="price">Price (USD)</FieldLabel>
                    <Input
                      id="price"
                      name="price"
                      type="number"
                      min="0.01"
                      step="0.01"
                      placeholder="24.99"
                      required
                    />
                  </Field>
                  <Field>
                    <FieldLabel htmlFor="stock">Stock quantity</FieldLabel>
                    <Input
                      id="stock"
                      name="stock"
                      type="number"
                      min="1"
                      step="1"
                      placeholder="10"
                      required
                    />
                  </Field>
                </div>

                <Field>
                  <FieldLabel htmlFor="destination">
                    Destination ZIP code
                  </FieldLabel>
                  <Input
                    id="destination"
                    name="destination"
                    type="number"
                    min="0"
                    step="1"
                    placeholder="94105"
                    required
                  />
                </Field>

                <Field>
                  <FieldLabel htmlFor="client_contact_email">
                    Client email
                  </FieldLabel>
                  <Input
                    id="client_contact_email"
                    name="client_contact_email"
                    type="email"
                    placeholder="client@example.com"
                    required
                  />
                </Field>

                <Field>
                  <FieldLabel htmlFor="client_contact_phone">
                    Client phone (optional)
                  </FieldLabel>
                  <Input
                    id="client_contact_phone"
                    name="client_contact_phone"
                    type="tel"
                    placeholder="Phone number"
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

                {submitProduct.isError && (
                  <p
                    className="rounded-xl bg-rose-50 px-4 py-3 text-sm text-rose-800"
                    role="alert"
                  >
                    {getSubmitErrorMessage(submitProduct.error)}
                  </p>
                )}

                {successMessage && (
                  <p
                    className="rounded-xl bg-emerald-50 px-4 py-3 text-sm text-emerald-800"
                    role="status"
                  >
                    {successMessage}
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
                    disabled={submitProduct.isPending}
                    className="h-10 rounded-full px-5"
                  >
                    {submitProduct.isPending
                      ? "Submitting..."
                      : "Submit product"}
                  </Button>
                </div>
              </form>
            </section>

            <aside className="rounded-3xl bg-emerald-950 p-6 text-white">
              <span className="flex size-11 items-center justify-center rounded-xl bg-white/10 text-lime-300">
                <ShieldCheck className="size-6" aria-hidden="true" />
              </span>
              <h3 className="mt-5 text-lg font-semibold">Before you submit</h3>
              <ul className="mt-4 space-y-3 text-sm leading-6 text-emerald-100/80">
                <li>Use the delivery ZIP code as the destination.</li>
                <li>Enter the product price in US dollars.</li>
                <li>
                  A delivery partner must be available for that destination.
                </li>
              </ul>
            </aside>
          </div>
        </main>
      </SidebarInset>
    </SidebarProvider>
  )
}

function getSubmitErrorMessage(error: unknown) {
  if (
    axios.isAxiosError(error) &&
    error.response?.status === 406
  ) {
    return "No delivery partner is currently available for this destination. Try another ZIP code."
  }

  return "The product could not be submitted. Check your details and try again."
}
