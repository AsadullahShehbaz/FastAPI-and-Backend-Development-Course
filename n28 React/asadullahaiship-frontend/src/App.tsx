import { useState } from "react"
import { useQuery } from "@tanstack/react-query"

import { Api } from "./api/client"

const api = new Api({
  baseURL: import.meta.env.VITE_API_BASE_URL,
})
// test_id = 89374580-8079-4782-86a1-7b6f4a2734be

function App() {
  const [productId, setProductId] = useState("89374580-8079-4782-86a1-7b6f4a2734be")

  const { data: product, isLoading, error } = useQuery({
    queryKey: ["product", productId],
    queryFn: async () => {
      const response = await api.product.getProduct(productId)
      return response.data
    },
  })
  if (isLoading || !product) {
      return <p role="status">Loading product…</p>
    }

  if (error) {
  return <p role="alert">{error.message}</p>
}

 return (
  <main>
    <label htmlFor="pid">Product ID</label>
    <input
      id="pid"
      value={productId}
      onChange={(event) => setProductId(event.target.value)}
    />

    <article>
      <h2>Product {product.id}</h2>
      <p>{product.name}</p>
      <p>Destination: {product.destination}</p>
      <p>Estimated delivery: {product.estimated_delivery ?? "Not available"}</p>
    </article>
  </main>
)

}

export default App