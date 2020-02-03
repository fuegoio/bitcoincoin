<template>
  <v-row>
    <v-col cols="12">
      <v-form class="px-3">
        <v-text-field
          v-model="buyingAmount"
          label="Amount Purchased"
          :rules="[
            v =>
              buyingAmountNotBiggerThanCashFlow(v) ||
              'Don\'t have enough cash flow',
          ]"
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
import axios from 'axios'

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
      axios
        .post('http://localhost:8000/api/v1/transactions', {
          user_id: this.user.id,
          currency_id: this.currency.id,
          quantity: this.buyingAmount,
          is_sale: false,
        })
        .then(response => {
          // Doit afficher que l'achat a bien été effectué
          // De même doit refresh
        })
        .catch(e => this.errors.push(e))
    },
    buyingAmountNotBiggerThanCashFlow(value) {
      return value * this.currency.last_value <= this.user.cash_flow
    },
  },
}
</script>

<style scoped></style>
