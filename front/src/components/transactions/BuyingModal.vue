<template>
  <div>
    <v-btn color="success" dark @click.stop.prevent="dialog = true">
      Acheter
    </v-btn>
    <v-dialog v-model="dialog" transition="slide-x-reverse-transition">
      <v-card class="buying-dialog">
        <v-row justify="center">
          <v-col class="currency-trend px-6" cols="8">
            <v-sparkline
              :value="value"
              auto-draw
              :gradient="gradient"
              gradient-direction="right"
              line-width="0.7"
              height="160"
              padding="12"
              stroke-linecap="round"
              smooth
            ></v-sparkline>
          </v-col>
          <v-col cols="4">
            <HeaderTransactionForm :currency="currency" />
            <v-col cols="12">
              <v-form class="px-3">
                <v-text-field
                  v-model="buyingAmount"
                  label="Amount Purchased"
                  :rules="[
                    v =>
                      (!isNaN(parseFloat(v)) && isFinite(v)) ||
                      'You have to type a number',
                    v =>
                      buyingAmountNotBiggerThanCashFlow(v) ||
                      'Don\'t have enough cash flow',
                  ]"
                ></v-text-field>
              </v-form>
            </v-col>
            <v-col cols="12">
              Predicted Cash Flow : {{ predictedCashFlowIfBuy | toCurrency }}
            </v-col>
            <v-btn color="success" class="mr-4" @click="validate">
              Acheter Crypto
            </v-btn>
          </v-col>
        </v-row>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import auth from '@/modules/auth'
import HeaderTransactionForm from './HeaderTransactionForm'
import axios from 'axios'
export default {
  name: 'BuyingModal',
  components: {
    HeaderTransactionForm,
  },
  props: {
    currency: Object,
  },
  data: function() {
    return {
      dialog: false,
      user: auth.user,
      buyingAmount: 0,
      value: [],
      gradient: ['#617be2', '#ff6473'],
    }
  },
  computed: {
    predictedCashFlowIfBuy: function() {
      return (
        this.user.profile.cash_flow -
        this.buyingAmount * this.currency.last_value
      )
    },
  },
  created() {
    this.getCurrencyRates()
  },
  methods: {
    validate() {
      axios
        .post('http://localhost:8000/api/v1/transactions', {
          currency: this.currency.id,
          quantity: this.buyingAmount,
          isSale: false,
        })
        .then(response => {
          this.dialog = false
          this.$emit('finished')
          this.buyingAmount = 0
          auth.checkAuth()
        })
        .catch(e => this.errors.push(e))
    },
    buyingAmountNotBiggerThanCashFlow(value) {
      return value * this.currency.last_value <= this.user.profile.cash_flow
    },
    getCurrencyRates() {
      axios
        .get(
          `http://localhost:8000/api/v1/currencies/${this.currency.id}/rates`,
          {
            params: { interval: 'hour', limit: 100 },
          },
        )
        .then(response => {
          this.value = response.data.map(x => x.value)
        })
        .catch(e => {})
    },
  },
}
</script>

<style scoped>
.buying-dialog {
  overflow-x: hidden;
}
</style>
