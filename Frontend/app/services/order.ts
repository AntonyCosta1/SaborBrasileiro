import { apiFetch } from "./api";

export async function getMyOrders(){
    return apiFetch("/orders/my");
}