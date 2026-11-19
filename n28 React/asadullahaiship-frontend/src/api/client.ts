/* eslint-disable */
/* tslint:disable */
// @ts-nocheck
/*
 * ---------------------------------------------------------------
 * ## THIS FILE WAS GENERATED VIA SWAGGER-TYPESCRIPT-API        ##
 * ##                                                           ##
 * ## AUTHOR: acacode                                           ##
 * ## SOURCE: https://github.com/acacode/swagger-typescript-api ##
 * ---------------------------------------------------------------
 */

/** TagName */
export enum TagName {
  Express = "express",
  Standard = "standard",
  Fragile = "fragile",
  Heavy = "heavy",
  International = "international",
  Domestic = "domestic",
  TemperatureControlled = "temperature_controlled",
  Gift = "gift",
  Return = "return",
  Documents = "documents",
}

/** ProductStatus */
export enum ProductStatus {
  Placed = "placed",
  InTransit = "in_transit",
  OutForDelivery = "out_for_delivery",
  Delivered = "delivered",
  Cancelled = "cancelled",
}

/** Body_login */
export interface BodyLogin {
  /** Grant Type */
  grant_type?: string | null;
  /** Username */
  username: string;
  /**
   * Password
   * @format password
   */
  password: string;
  /**
   * Scope
   * @default ""
   */
  scope?: string;
  /** Client Id */
  client_id?: string | null;
  /**
   * Client Secret
   * @format password
   */
  client_secret?: string | null;
}

/** Body_login_delivery_partner */
export interface BodyLoginDeliveryPartner {
  /** Grant Type */
  grant_type?: string | null;
  /** Username */
  username: string;
  /**
   * Password
   * @format password
   */
  password: string;
  /**
   * Scope
   * @default ""
   */
  scope?: string;
  /** Client Id */
  client_id?: string | null;
  /**
   * Client Secret
   * @format password
   */
  client_secret?: string | null;
}

/** Body_reset_password */
export interface BodyResetPassword {
  /** Password */
  password: string;
}

/** Body_submit_review */
export interface BodySubmitReview {
  /**
   * Rating
   * @min 1
   * @max 5
   */
  rating: number;
  /** Comment */
  comment?: string | null;
}

/** DeliveryPartnerCreate */
export interface DeliveryPartnerCreate {
  /** Name */
  name: string;
  /**
   * Email
   * @format email
   */
  email: string;
  /** Serviceable Zip Codes */
  serviceable_zip_codes: number[];
  /** Max Handling Capacity */
  max_handling_capacity: number;
  /** Password */
  password: string;
}

/** DeliveryPartnerRead */
export interface DeliveryPartnerRead {
  /** Name */
  name: string;
  /**
   * Email
   * @format email
   */
  email: string;
  /** Serviceable Zip Codes */
  serviceable_zip_codes: number[];
  /** Max Handling Capacity */
  max_handling_capacity: number;
}

/** DeliveryPartnerUpdate */
export interface DeliveryPartnerUpdate {
  /** Serviceable Zip Codes */
  serviceable_zip_codes?: number[] | null;
  /** Max Handling Capacity */
  max_handling_capacity?: number | null;
}

/** HTTPValidationError */
export interface HTTPValidationError {
  /** Detail */
  detail?: ValidationError[];
}

/** ProductCreate */
export interface ProductCreate {
  /**
   * Name
   * Product title
   * @minLength 3
   * @maxLength 100
   */
  name: string;
  /**
   * Price
   * Price is USD
   * @exclusiveMin 0
   */
  price: number;
  /**
   * Stock
   * Unit available in warehouse
   * @exclusiveMin 0
   */
  stock: number;
  /**
   * Destination
   * Zip Code of Product Destination
   */
  destination: number;
  /**
   * Client Contact Email
   * @format email
   */
  client_contact_email: string;
  /** Client Contact Phone */
  client_contact_phone?: string | null;
}

/** ProductEvent */
export interface ProductEvent {
  /**
   * Id
   * @format uuid
   */
  id: string;
  /**
   * Created At
   * @format date-time
   */
  created_at: string;
  /** Location */
  location: number;
  status: ProductStatus;
  /** Description */
  description?: string | null;
  /**
   * Product Id
   * @format uuid
   */
  product_id: string;
}

/** ProductRead */
export interface ProductRead {
  /**
   * Name
   * Product title
   * @minLength 3
   * @maxLength 100
   */
  name: string;
  /**
   * Price
   * Price is USD
   * @exclusiveMin 0
   */
  price: number;
  /**
   * Stock
   * Unit available in warehouse
   * @exclusiveMin 0
   */
  stock: number;
  /**
   * Destination
   * Zip Code of Product Destination
   */
  destination: number;
  /**
   * Id
   * @format uuid
   */
  id: string;
  status: ProductStatus;
  /**
   * Estimated Delivery
   * @deprecated
   * @format date-time
   */
  estimated_delivery: string;
  seller: SellerRead;
  /** Timeline */
  timeline: ProductEvent[];
  /** Tags */
  tags: TagRead[];
}

/** ProductUpdate */
export interface ProductUpdate {
  status?: ProductStatus | null;
  /** Location */
  location?: number | null;
  /** Description */
  description?: string | null;
  /** Estimated Delivery */
  estimated_delivery?: string | null;
}

/** SellerCreate */
export interface SellerCreate {
  /** Name */
  name: string;
  /**
   * Email
   * @format email
   */
  email: string;
  /** Address */
  address?: string | null;
  /** Zip Code */
  zip_code?: number | null;
  /** Password */
  password: string;
}

/** SellerRead */
export interface SellerRead {
  /** Name */
  name: string;
  /**
   * Email
   * @format email
   */
  email: string;
  /** Address */
  address?: string | null;
  /** Zip Code */
  zip_code?: number | null;
}

/** TagRead */
export interface TagRead {
  name: TagName;
  /** Instruction */
  instruction: string;
}

/** ValidationError */
export interface ValidationError {
  /** Location */
  loc: (string | number)[];
  /** Message */
  msg: string;
  /** Error Type */
  type: string;
  /** Input */
  input?: any;
  /** Context */
  ctx?: object;
}

import type {
  AxiosInstance,
  AxiosRequestConfig,
  AxiosResponse,
  HeadersDefaults,
  ResponseType,
} from "axios";
import axios from "axios";

export type QueryParamsType = Record<string | number, any>;

export interface FullRequestParams
  extends Omit<AxiosRequestConfig, "data" | "params" | "url" | "responseType"> {
  /** set parameter to `true` for call `securityWorker` for this request */
  secure?: boolean;
  /** request path */
  path: string;
  /** content type of request body */
  type?: ContentType;
  /** query params */
  query?: QueryParamsType;
  /** format of response (i.e. response.json() -> format: "json") */
  format?: ResponseType;
  /** request body */
  body?: unknown;
}

export type RequestParams = Omit<
  FullRequestParams,
  "body" | "method" | "query" | "path"
>;

export interface ApiConfig<SecurityDataType = unknown>
  extends Omit<AxiosRequestConfig, "data" | "cancelToken"> {
  securityWorker?: (
    securityData: SecurityDataType | null,
  ) => Promise<AxiosRequestConfig | void> | AxiosRequestConfig | void;
  secure?: boolean;
  format?: ResponseType;
}

export enum ContentType {
  Json = "application/json",
  JsonApi = "application/vnd.api+json",
  FormData = "multipart/form-data",
  UrlEncoded = "application/x-www-form-urlencoded",
  Text = "text/plain",
}

export class HttpClient<SecurityDataType = unknown> {
  public instance: AxiosInstance;
  private securityData: SecurityDataType | null = null;
  private securityWorker?: ApiConfig<SecurityDataType>["securityWorker"];
  private secure?: boolean;
  private format?: ResponseType;

  constructor({
    securityWorker,
    secure,
    format,
    ...axiosConfig
  }: ApiConfig<SecurityDataType> = {}) {
    this.instance = axios.create({
      ...axiosConfig,
      baseURL: axiosConfig.baseURL || "",
    });
    this.secure = secure;
    this.format = format;
    this.securityWorker = securityWorker;
  }

  public setSecurityData = (data: SecurityDataType | null) => {
    this.securityData = data;
  };

  protected mergeRequestParams(
    params1: AxiosRequestConfig,
    params2?: AxiosRequestConfig,
  ): AxiosRequestConfig {
    const method = params1.method || (params2 && params2.method);

    return {
      ...this.instance.defaults,
      ...params1,
      ...(params2 || {}),
      headers: {
        ...((method &&
          this.instance.defaults.headers[
            method.toLowerCase() as keyof HeadersDefaults
          ]) ||
          {}),
        ...(params1.headers || {}),
        ...((params2 && params2.headers) || {}),
      },
    };
  }

  protected stringifyFormItem(formItem: unknown) {
    if (typeof formItem === "object" && formItem !== null) {
      return JSON.stringify(formItem);
    } else {
      return `${formItem}`;
    }
  }

  protected createFormData(input: Record<string, unknown>): FormData {
    if (input instanceof FormData) {
      return input;
    }
    return Object.keys(input || {}).reduce((formData, key) => {
      const property = input[key];
      const propertyContent: any[] =
        property instanceof Array ? property : [property];

      for (const formItem of propertyContent) {
        const isFileType = formItem instanceof Blob || formItem instanceof File;
        formData.append(
          key,
          isFileType ? formItem : this.stringifyFormItem(formItem),
        );
      }

      return formData;
    }, new FormData());
  }

  public request = async <T = any, _E = any>({
    secure,
    path,
    type,
    query,
    format,
    body,
    ...params
  }: FullRequestParams): Promise<AxiosResponse<T>> => {
    const secureParams =
      ((typeof secure === "boolean" ? secure : this.secure) &&
        this.securityWorker &&
        (await this.securityWorker(this.securityData))) ||
      {};
    const requestParams = this.mergeRequestParams(params, secureParams);
    const responseFormat = format || this.format || undefined;

    if (
      type === ContentType.FormData &&
      body &&
      body !== null &&
      typeof body === "object"
    ) {
      body = this.createFormData(body as Record<string, unknown>);
    }

    if (
      type === ContentType.Text &&
      body &&
      body !== null &&
      typeof body !== "string"
    ) {
      body = JSON.stringify(body);
    }

    return this.instance.request({
      ...requestParams,
      headers: {
        ...(requestParams.headers || {}),
        ...(type ? { "Content-Type": type } : {}),
      },
      params: query,
      responseType: responseFormat,
      data: body,
      url: path,
    });
  };
}

/**
 * @title AsadullahAIShip API
 * @version 1.0.0
 * @termsOfService http://asadullahaiship.com/terms_of_services
 * @contact AsadullahAIShip Support <support@asadullahaiship.example.com> (https://asadullahaiship.example.com/support)
 *
 * AsadullahAIShip helps sellers and delivery partners manage deliveries.
 *
 * ### For sellers
 * - Submit products for delivery.
 * - Share tracking links with customers.
 *
 * ### For delivery partners
 * - Accept available deliveries.
 * - Track and update delivery status.
 * - Send status notifications.
 *
 */
export class Api<
  SecurityDataType extends unknown,
> extends HttpClient<SecurityDataType> {
  /**
   * No description
   *
   * @name Home
   * @summary Home
   * @request GET:/
   */
  home = (params: RequestParams = {}) =>
    this.request<any, any>({
      path: `/`,
      method: "GET",
      format: "json",
      ...params,
    });

  seller = {
    /**
     * No description
     *
     * @tags Seller
     * @name RegisterSeller
     * @summary Register Seller
     * @request POST:/seller/signup
     */
    registerSeller: (data: SellerCreate, params: RequestParams = {}) =>
      this.request<SellerRead, HTTPValidationError>({
        path: `/seller/signup`,
        method: "POST",
        body: data,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Seller
     * @name Login
     * @summary Login
     * @request POST:/seller/login
     */
    login: (data: BodyLogin, params: RequestParams = {}) =>
      this.request<Record<string, any>, HTTPValidationError>({
        path: `/seller/login`,
        method: "POST",
        body: data,
        type: ContentType.UrlEncoded,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Seller
     * @name LogoutSeller
     * @summary Logout Seller
     * @request GET:/seller/logout
     * @secure
     */
    logoutSeller: (params: RequestParams = {}) =>
      this.request<any, any>({
        path: `/seller/logout`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Seller
     * @name VerifySellerEmail
     * @summary Verify Seller Email
     * @request GET:/seller/verify
     */
    verifySellerEmail: (
      query: {
        /** Token */
        token: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/seller/verify`,
        method: "GET",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Seller
     * @name ForgotPassword
     * @summary Forgot Password
     * @request GET:/seller/forgot_password
     */
    forgotPassword: (
      query: {
        /**
         * Email
         * @format email
         */
        email: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/seller/forgot_password`,
        method: "GET",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Seller
     * @name ResetPasswordForm
     * @summary Reset Password Form
     * @request GET:/seller/reset_password_form
     */
    resetPasswordForm: (
      query: {
        /** Token */
        token: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/seller/reset_password_form`,
        method: "GET",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Seller
     * @name ResetPassword
     * @summary Reset Password
     * @request POST:/seller/reset_password
     */
    resetPassword: (
      query: {
        /** Token */
        token: string;
      },
      data: BodyResetPassword,
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/seller/reset_password`,
        method: "POST",
        query: query,
        body: data,
        type: ContentType.UrlEncoded,
        format: "json",
        ...params,
      }),
  };
  product = {
    /**
     * No description
     *
     * @tags Product
     * @name AddTagToProduct
     * @summary Add Tag To Product
     * @request POST:/product/v1/tag
     */
    addTagToProduct: (
      query: {
        /**
         * Id
         * @format uuid
         */
        id: string;
        tag_name: TagName;
      },
      params: RequestParams = {},
    ) =>
      this.request<ProductRead, HTTPValidationError>({
        path: `/product/v1/tag`,
        method: "POST",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Product
     * @name RemoveTagFromProduct
     * @summary Remove Tag From Product
     * @request DELETE:/product/v1/tag
     */
    removeTagFromProduct: (
      query: {
        /**
         * Id
         * @format uuid
         */
        id: string;
        tag_name: TagName;
      },
      params: RequestParams = {},
    ) =>
      this.request<ProductRead, HTTPValidationError>({
        path: `/product/v1/tag`,
        method: "DELETE",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Product
     * @name GetProductsByTag
     * @summary Get Products By Tag
     * @request GET:/product/v1/tagged
     */
    getProductsByTag: (
      query: {
        tag_name: TagName;
      },
      params: RequestParams = {},
    ) =>
      this.request<ProductRead[], HTTPValidationError>({
        path: `/product/v1/tagged`,
        method: "GET",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Product
     * @name SubmitReview
     * @summary Submit Review
     * @request POST:/product/v1/review
     */
    submitReview: (
      query: {
        /** Token */
        token: string;
      },
      data: BodySubmitReview,
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/product/v1/review`,
        method: "POST",
        query: query,
        body: data,
        type: ContentType.UrlEncoded,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Product
     * @name GetReviewForm
     * @summary Get Review Form
     * @request GET:/product/v1/review
     */
    getReviewForm: (
      query: {
        /** Token */
        token: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/product/v1/review`,
        method: "GET",
        query: query,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Product
     * @name GetProduct
     * @summary Get Product
     * @request GET:/product/v1/{id}
     */
    getProduct: (id: string, params: RequestParams = {}) =>
      this.request<ProductRead, HTTPValidationError>({
        path: `/product/v1/${id}`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * @description Submit a product for delivery. **Sellers** can track it after creation.
     *
     * @tags Product
     * @name CreateProduct
     * @summary Create a product
     * @request POST:/product/v1/
     * @secure
     */
    createProduct: (data: ProductCreate, params: RequestParams = {}) =>
      this.request<ProductRead, void | HTTPValidationError>({
        path: `/product/v1/`,
        method: "POST",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Product
     * @name PatchProduct
     * @summary Patch Product
     * @request PATCH:/product/v1/
     * @secure
     */
    patchProduct: (
      query: {
        /**
         * Id
         * @format uuid
         */
        id: string;
      },
      data: ProductUpdate,
      params: RequestParams = {},
    ) =>
      this.request<ProductRead, HTTPValidationError>({
        path: `/product/v1/`,
        method: "PATCH",
        query: query,
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Product
     * @name CancelProduct
     * @summary Cancel Product
     * @request DELETE:/product/v1/
     * @secure
     */
    cancelProduct: (
      query: {
        /**
         * Id
         * @format uuid
         */
        id: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<ProductRead, HTTPValidationError>({
        path: `/product/v1/`,
        method: "DELETE",
        query: query,
        secure: true,
        format: "json",
        ...params,
      }),
  };
  partner = {
    /**
     * No description
     *
     * @tags Delivery Partner
     * @name UpdateDeliveryPartner
     * @summary Update Delivery Partner
     * @request POST:/partner/
     * @secure
     */
    updateDeliveryPartner: (
      data: DeliveryPartnerUpdate,
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/partner/`,
        method: "POST",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Delivery Partner
     * @name RegisterDeliveryPartner
     * @summary Register Delivery Partner
     * @request POST:/partner/signup
     */
    registerDeliveryPartner: (
      data: DeliveryPartnerCreate,
      params: RequestParams = {},
    ) =>
      this.request<DeliveryPartnerRead, HTTPValidationError>({
        path: `/partner/signup`,
        method: "POST",
        body: data,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Delivery Partner
     * @name LoginDeliveryPartner
     * @summary Login Delivery Partner
     * @request POST:/partner/login
     */
    loginDeliveryPartner: (
      data: BodyLoginDeliveryPartner,
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/partner/login`,
        method: "POST",
        body: data,
        type: ContentType.UrlEncoded,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags Delivery Partner
     * @name VerifyPartnerEmail
     * @summary Verify Partner Email
     * @request GET:/partner/verify
     */
    verifyPartnerEmail: (
      query: {
        /** Token */
        token: string;
      },
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/partner/verify`,
        method: "GET",
        query: query,
        format: "json",
        ...params,
      }),
  };
}
