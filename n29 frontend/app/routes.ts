import { type RouteConfig, index, route } from "@react-router/dev/routes";

export default [
  index("routes/home.tsx"),
  route("/dashboard", "routes/dashboard.tsx"),
  route("/account", "routes/account.tsx"),
  route("/products/:id", "routes/products/detail.tsx"),
  route("/seller/products/new", "routes/seller/products/new.tsx"),
  route("/partner/products/update", "routes/partner/products/update.tsx"),
  route("/seller/login", "routes/seller/login.tsx"),
  route("/partner/login", "routes/partner/login.tsx"),
] satisfies RouteConfig;
