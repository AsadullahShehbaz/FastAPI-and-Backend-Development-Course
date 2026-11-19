import { LoaderCircleIcon } from "lucide-react"

export default function Loading() {
  return (
    <div
      className="flex items-center justify-center gap-2 p-6 text-muted-foreground"
      role="status"
    >
      <LoaderCircleIcon className="size-5 animate-spin" />
      <span>Loading...</span>
    </div>
  )
}
