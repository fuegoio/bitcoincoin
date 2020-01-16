<template>
  <v-row>
    <v-col cols="12">
      <v-form class="px-3">
        <v-text-field
          label="Amount Purchased"
          v-model="buyingAmount"
        ></v-text-field>
      </v-form>
    </v-col>
    <v-col cols="4">
      Predicted Cash Flow
    </v-col>
    <v-col class="text-center" cols="8">
      {{ predictedCashFlowIfBuy | toCurrency }}
    </v-col>
    <v-btn color="success" class="mr-4" @click="validate">
      Acheter Crypto
    </v-btn>
  </v-row>
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
      return this.user.cash_flow - this.buyingAmount * this.currency.last_value
    },
  },
  methods: {
    validate() {
      return true
    },
  },
}
</script>

<style scoped></style>
