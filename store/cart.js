import { defineStore } from "pinia";
import { useToast } from "vue-toastification";

const toast = useToast();

export const useCart = defineStore("cart", {
  state: () => {
    return {
      cart: [],
    };
  },
  getters: {
    count(state) {
      return state.cart.length;
    },
    allItems(state) {
      return state.cart;
    },
    totalAmount(state) {
      return state.cart.reduce((acc, product) => {
        return acc + product.price * product.qty;
      }, 0);
    },
  },
  actions: {
    addToCart(product) {
      const item = this.cart.find((p) => p.id == product.id);
      if (!item) {
        this.cart.push({
          ...product,
          qty: 1,
        });
      } else {
        item.qty++;
      }
      toast.success("محصولت با موفقیت به سبدت اضاف شد 🤩");
    },
    remove(id) {
      this.cart = this.cart.filter((p) => p.id != id);
    },
    increment(id) {
      const item = this.cart.find((p) => p.id == id);
      if (item) {
        item.qty++;
      }
    },
    decrement(id) {
      const item = this.cart.find((p) => p.id == id);
      if (item) {
        if (item.quantity > 1) {
          item.qty--;
        }
      }
    },
    clearCart() {
      this.cart = [];
    },
  },
  persist: {
    storage: persistedState.localStorage,
  },
});
