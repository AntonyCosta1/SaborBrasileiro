export { apiFetch } from "./api";

export async function getMenuItens(){
    return apiFetch("/menu");
}