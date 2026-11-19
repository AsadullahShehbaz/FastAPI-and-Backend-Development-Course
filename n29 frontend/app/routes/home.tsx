import {
  ArrowRight,
  ArrowUpRight,
  Check,
  MapPin,
  PackageCheck,
  Store,
  Truck,
} from "lucide-react"
import { Link } from "react-router"

import { buttonVariants } from "~/components/ui/button"

export default function Home() {
  return (
    <main className="min-h-svh overflow-hidden bg-[#f7f8f5] text-slate-950">
      <header className="mx-auto flex max-w-7xl items-center justify-between px-6 py-5 lg:px-10">
        <Link to="/" className="flex items-center gap-3" aria-label="AsadullahAIShip home">
          <span className="flex size-10 items-center justify-center rounded-xl bg-emerald-900 text-white">
            <PackageCheck className="size-5" aria-hidden="true" />
          </span>
          <span className="text-lg font-bold tracking-tight">AsadullahAIShip</span>
        </Link>

        <nav className="flex items-center gap-3">
          <a
            href="#workspaces"
            className="hidden rounded-full px-4 py-2 text-sm font-medium text-slate-600 transition hover:text-emerald-900 sm:inline-flex"
          >
            Explore
          </a>
          <Link
            to="/seller/login"
            className={buttonVariants({
              className: "h-10 rounded-full bg-emerald-900 px-5 text-white hover:bg-emerald-800",
            })}
          >
            Sign in <ArrowUpRight aria-hidden="true" />
          </Link>
        </nav>
      </header>

      <section className="mx-auto grid max-w-7xl items-center gap-12 px-6 pb-16 pt-10 md:pb-24 md:pt-16 lg:grid-cols-2 lg:gap-16 lg:px-10">
        <div>
          <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-emerald-900/10 bg-white/80 px-3.5 py-2 text-sm font-medium text-emerald-900 shadow-sm">
            <span className="size-2 rounded-full bg-emerald-500" />
            A simpler way to ship
          </div>
          <h1 className="max-w-2xl text-5xl leading-[1.08] font-semibold tracking-tight sm:text-6xl lg:text-7xl">
            Good things are
            <br />
            on their <span className="font-serif font-normal italic text-emerald-800">way.</span>
          </h1>
          <p className="mt-6 max-w-xl text-lg leading-8 text-slate-600">
            Keep your products moving with one easy place for sellers and
            delivery partners to manage their work.
          </p>

          <div className="mt-8 flex flex-col gap-3 sm:flex-row">
            <Link
              to="/seller/login"
              className={buttonVariants({
                size: "lg",
                className: "h-12 rounded-full bg-emerald-900 px-6 text-white hover:bg-emerald-800",
              })}
            >
              I&apos;m a seller <ArrowRight aria-hidden="true" />
            </Link>
            <Link
              to="/partner/login"
              className={buttonVariants({
                size: "lg",
                variant: "outline",
                className: "h-12 rounded-full border-slate-300 bg-white px-6 hover:border-emerald-900 hover:text-emerald-900",
              })}
            >
              I&apos;m a delivery partner
            </Link>
          </div>

          <div className="mt-8 flex flex-wrap gap-x-6 gap-y-3 text-sm text-slate-600">
            <span className="inline-flex items-center gap-2">
              <Check className="size-4 text-emerald-700" aria-hidden="true" />
              Easy to get started
            </span>
            <span className="inline-flex items-center gap-2">
              <Check className="size-4 text-emerald-700" aria-hidden="true" />
              Built for your workflow
            </span>
          </div>
        </div>

        <div className="relative mx-auto w-full max-w-xl">
          <div
            className="absolute -right-10 -top-10 size-40 rounded-full bg-lime-200/70 blur-3xl"
            aria-hidden="true"
          />
          <div
            className="absolute -bottom-10 -left-10 size-40 rounded-full bg-emerald-200/70 blur-3xl"
            aria-hidden="true"
          />
          <div className="relative rounded-[2rem] border border-white bg-white p-4 shadow-[0_24px_80px_-28px_rgba(15,50,35,0.28)] sm:p-6">
            <div className="flex items-center justify-between px-1 pb-5">
              <div>
                <p className="text-sm font-semibold">Your shipping workspace</p>
                <p className="mt-1 text-xs text-slate-500">A smoother journey, from start to finish</p>
              </div>
              <span className="flex size-10 items-center justify-center rounded-full bg-emerald-50 text-emerald-800">
                <PackageCheck className="size-5" aria-hidden="true" />
              </span>
            </div>

            <div className="overflow-hidden rounded-3xl bg-emerald-950 p-6 text-white sm:p-8">
              <div className="flex items-center justify-between">
                <span className="text-xs font-medium tracking-[0.18em] text-emerald-200 uppercase">
                  Made for moving forward
                </span>
                <span className="size-2.5 rounded-full bg-lime-300" />
              </div>
              <div className="mt-10 flex items-center justify-between gap-4">
                <div>
                  <p className="text-sm text-emerald-200">From your store</p>
                  <p className="mt-1 text-lg font-semibold">Ready to go</p>
                </div>
                <div className="flex flex-1 items-center px-2">
                  <span className="size-3 rounded-full border-2 border-lime-300" />
                  <span className="h-px flex-1 border-t border-dashed border-emerald-500" />
                  <Truck className="mx-2 size-6 shrink-0 text-lime-300" aria-hidden="true" />
                  <span className="h-px flex-1 border-t border-dashed border-emerald-500" />
                  <MapPin className="size-5 shrink-0 text-lime-300" aria-hidden="true" />
                </div>
                <div className="text-right">
                  <p className="text-sm text-emerald-200">To their door</p>
                  <p className="mt-1 text-lg font-semibold">On its way</p>
                </div>
              </div>
              <div className="mt-8 rounded-2xl border border-white/10 bg-white/10 p-4">
                <div className="flex items-center gap-3">
                  <span className="flex size-10 items-center justify-center rounded-xl bg-lime-300 text-emerald-950">
                    <PackageCheck className="size-5" aria-hidden="true" />
                  </span>
                  <div>
                    <p className="text-sm font-semibold">Every step, in one place</p>
                    <p className="mt-1 text-xs text-emerald-100/75">
                      Simple tools for your shipping journey
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <div className="grid gap-3 pt-4 sm:grid-cols-2">
              <div className="flex items-center gap-3 rounded-2xl bg-[#f7f8f5] p-4">
                <span className="flex size-10 items-center justify-center rounded-xl bg-white text-emerald-800 shadow-sm">
                  <Store className="size-5" aria-hidden="true" />
                </span>
                <div>
                  <p className="text-sm font-semibold">For sellers</p>
                  <p className="text-xs text-slate-500">Manage your products</p>
                </div>
              </div>
              <div className="flex items-center gap-3 rounded-2xl bg-[#f7f8f5] p-4">
                <span className="flex size-10 items-center justify-center rounded-xl bg-white text-emerald-800 shadow-sm">
                  <Truck className="size-5" aria-hidden="true" />
                </span>
                <div>
                  <p className="text-sm font-semibold">For partners</p>
                  <p className="text-xs text-slate-500">Keep deliveries moving</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="workspaces" className="border-t border-slate-200/80 bg-white">
        <div className="mx-auto max-w-7xl px-6 py-16 lg:px-10 lg:py-20">
          <div className="mx-auto max-w-2xl text-center">
            <p className="text-sm font-semibold tracking-[0.16em] text-emerald-800 uppercase">
              One platform, two ways to get moving
            </p>
            <h2 className="mt-3 text-3xl font-semibold tracking-tight sm:text-4xl">
              Choose your workspace
            </h2>
            <p className="mt-4 leading-7 text-slate-600">
              Sign in to the space that fits the work you do.
            </p>
          </div>

          <div className="mx-auto mt-10 grid max-w-4xl gap-5 md:grid-cols-2">
            <div className="rounded-3xl border border-slate-200 bg-[#fbfcfa] p-6 sm:p-8">
              <span className="flex size-12 items-center justify-center rounded-2xl bg-emerald-100 text-emerald-900">
                <Store className="size-6" aria-hidden="true" />
              </span>
              <h3 className="mt-5 text-xl font-semibold">For sellers</h3>
              <p className="mt-2 min-h-14 leading-6 text-slate-600">
                Keep your product details and shipping work organized in one
                place.
              </p>
              <Link
                to="/seller/login"
                className={buttonVariants({
                  variant: "outline",
                  className: "mt-6 h-10 rounded-full border-slate-300 bg-white px-5",
                })}
              >
                Seller sign in <ArrowRight aria-hidden="true" />
              </Link>
            </div>

            <div className="rounded-3xl border border-slate-200 bg-[#fbfcfa] p-6 sm:p-8">
              <span className="flex size-12 items-center justify-center rounded-2xl bg-lime-100 text-emerald-900">
                <Truck className="size-6" aria-hidden="true" />
              </span>
              <h3 className="mt-5 text-xl font-semibold">For delivery partners</h3>
              <p className="mt-2 min-h-14 leading-6 text-slate-600">
                Access your partner account and the tools you need for your
                delivery work.
              </p>
              <Link
                to="/partner/login"
                className={buttonVariants({
                  variant: "outline",
                  className: "mt-6 h-10 rounded-full border-slate-300 bg-white px-5",
                })}
              >
                Partner sign in <ArrowRight aria-hidden="true" />
              </Link>
            </div>
          </div>
        </div>
      </section>

      <footer className="mx-auto flex max-w-7xl flex-col gap-2 px-6 py-6 text-sm text-slate-500 sm:flex-row sm:items-center sm:justify-between lg:px-10">
        <p>AsadullahAIShip</p>
        <p>Making every delivery a little simpler.</p>
      </footer>
    </main>
  )
}
