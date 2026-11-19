import { Api } from "~/api/client"

const api = new Api<string>({
  baseURL: "http://localhost:8000",
  securityWorker: (token) => {
    if (!token) {
      return {}
    }

    return {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  },
})

export default api
