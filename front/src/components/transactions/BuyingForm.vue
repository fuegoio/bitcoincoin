<template>
  <v-form class="px-3">
    <v-text-field label="Amount" v-model="buyingAmount"></v-text-field>
    {{ predictedCashFlowIfBuy | toCurrency }}
  </v-form>
</template>

<script>
import auth from '@/modules/auth'
export default {
  name: 'BuyingForm',
  props: {
    currency: Object,
  },
  data: () => {
    return {
      buyingAmount: 0,
      user: auth.user.profile,
    }
  },
  computed: {
    predictedCashFlowIfBuy: function() {
      return this.user.cash_flow - this.buyingAmount * this.currency.lastValue
    },
  },
}
</script>

<style scoped></style>
