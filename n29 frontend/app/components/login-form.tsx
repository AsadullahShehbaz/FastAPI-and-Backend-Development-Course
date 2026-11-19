import { cn } from "cn"

import { Button } from "~/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "~/components/ui/card"
import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLabel,
} from "~/components/ui/field"
import { Input } from "~/components/ui/input"

import { useContext } from "react"
import { AuthContext, type AccountType } from "~/context/auth-context"
import { toast } from "sonner"



export function LoginForm({
  className,
  accountType = "seller",
  ...props
}: React.ComponentProps<"div"> & { accountType?: AccountType }) {


    const { login } = useContext(AuthContext)
    async function loginUser(formData: FormData) {
      const email = formData.get("email")
      const password = formData.get("password")

      if (!email || !password) {
      return
    }

  try {
    await login(email.toString(), password.toString(), accountType)
    console.log("Login successful")
    toast.success("Login successful")
  } catch (error) {
    console.error(error)
    toast.error("Login failed. Please check your credentials.")

  }
    }

  return (
    <div className={cn("flex flex-col gap-6", className)} {...props}>
      <Card>
        <CardHeader>
          <CardTitle>Login to your account</CardTitle>
          <CardDescription>
            Enter your email below to login to your account
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form action={loginUser}>
            <FieldGroup>
              <Field>
                <FieldLabel htmlFor="email">Email</FieldLabel>
                <Input
                  id="email"
                  type="email"
                  name="email"
                  placeholder="m@example.com"
                  required
                />
              </Field>
              <Field>
                <div className="flex items-center">
                  <FieldLabel htmlFor="password">Password</FieldLabel>
                  <a
                    href="#"
                    className="ml-auto inline-block text-sm underline-offset-4 hover:underline"
                  >
                    Forgot your password?
                  </a>
                </div>
                <Input id="password" type="password" name="password" required />
              </Field>
              <Field>
                <Button type="submit">Login</Button>
                <Button variant="outline" type="button">
                  Login with Google
                </Button>
                <FieldDescription className="text-center">
                  Don&apos;t have an account? <a href="#">Sign up</a>
                </FieldDescription>
              </Field>
            </FieldGroup>
          </form>
        </CardContent>
      </Card>
    </div>
  )
}
