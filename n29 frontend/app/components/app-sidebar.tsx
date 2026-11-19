import * as React from "react"
import { GalleryVerticalEndIcon, PackagePlus, Truck } from "lucide-react"

import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "~/components/ui/sidebar"
import { AuthContext } from "~/context/auth-context"

const data = {
  navMain: [
    {
      title: "Dashboard",
      url: "/dashboard",
    },
    {
      title: "Account",
      url: "/account",
    },
  ],
}

export function AppSidebar({
  currentRoute,
  ...props
}: React.ComponentProps<typeof Sidebar> & { currentRoute?: string }) {
  const { user } = React.useContext(AuthContext)

  return (
    <Sidebar variant="floating" {...props}>
      <SidebarHeader>
        <SidebarMenu>
          <SidebarMenuItem>
            <SidebarMenuButton size="lg" render={<a href="/" />}>
              <div className="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
                <GalleryVerticalEndIcon className="size-4" />
              </div>
              <div className="flex flex-col gap-0.5 leading-none">
                <span className="font-medium">AsadullahAIShip</span>
                <span>v1.0.0</span>
              </div>
            </SidebarMenuButton>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarHeader>
      <SidebarContent>
        <SidebarGroup>
          <SidebarMenu className="gap-2">
            {data.navMain.map((item) => (
              <SidebarMenuItem key={item.title}>
                <SidebarMenuButton
                  isActive={item.title === currentRoute}
                  render={<a href={item.url} className="font-medium" />}
                >
                  {item.title}
                </SidebarMenuButton>
              </SidebarMenuItem>
            ))}
            {user === "seller" && (
              <SidebarMenuItem>
                <SidebarMenuButton
                  isActive={currentRoute === "Submit product"}
                  render={
                    <a
                      href="/seller/products/new"
                      className="font-medium"
                    />
                  }
                >
                  <PackagePlus className="size-4" aria-hidden="true" />
                  Submit product
                </SidebarMenuButton>
              </SidebarMenuItem>
            )}
            {user === "partner" && (
              <SidebarMenuItem>
                <SidebarMenuButton
                  isActive={currentRoute === "Update product"}
                  render={
                    <a
                      href="/partner/products/update"
                      className="font-medium"
                    />
                  }
                >
                  <Truck className="size-4" aria-hidden="true" />
                  Update product
                </SidebarMenuButton>
              </SidebarMenuItem>
            )}
          </SidebarMenu>
        </SidebarGroup>
      </SidebarContent>
    </Sidebar>
  )
}
