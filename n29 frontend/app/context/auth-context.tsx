import {
  createContext,
  useEffect,
  useState,
  type ReactNode,
} from "react"
import { useNavigate } from "react-router"

import api from "~/lib/api"

export type AccountType = "seller" | "partner"

export interface AuthContextType {
  token?: string | null
  user?: AccountType | null
  login: (
    email: string,
    password: string,
    accountType: AccountType
  ) => Promise<void>
  logout: () => Promise<void>
}

export const AuthContext = createContext<AuthContextType>({
  token: null,
  user: null,
  login: async () => {},
  logout: async () => {},
})

interface AuthProviderProps {
  children: ReactNode
}

export function AuthProvider({ children }: AuthProviderProps) {
  const [token, setToken] = useState<string | null>()
  const [user, setUser] = useState<AccountType | null>(null)
  const navigate = useNavigate()

  useEffect(() => {
    const storedToken = localStorage.getItem("token")
    const storedUser = localStorage.getItem("user")

    if (storedToken) {
      setToken(storedToken)
      api.setSecurityData(storedToken)
    } else {
      setToken(null)
    }

    if (storedUser === "seller" || storedUser === "partner") {
      setUser(storedUser)
    } else {
      setUser(null)
    }
  }, [])

  async function login(
    email: string,
    password: string,
    accountType: AccountType
  ) {
    const credentials = {
      username: email,
      password,
    }

    const { data } =
      accountType === "partner"
        ? await api.partner.loginDeliveryPartner(credentials)
        : await api.seller.login(credentials)

    const accessToken = data?.access_token

    if (accessToken) {
      setToken(accessToken)
      setUser(accountType)
      api.setSecurityData(accessToken)
      localStorage.setItem("token", accessToken)
      localStorage.setItem("user", accountType)
      navigate("/dashboard")
    }
  }

  async function logout() {
    if (user === "partner") {
      await api.partner.logoutPartner()
    } else if (user === "seller") {
      await api.seller.logoutSeller()
    }

    setToken(null)
    setUser(null)
    api.setSecurityData(null)
    localStorage.removeItem("token")
    localStorage.removeItem("user")
  }

  return (
    <AuthContext.Provider value={{ token, user, login, logout }}>
      {token === undefined ? <div>Loading...</div> : children}
    </AuthContext.Provider>
  )
}
