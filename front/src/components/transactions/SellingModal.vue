<template>
  <div>
    <v-btn color="accent" dark @click.stop.prevent="dialog = true">
      Vendre
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
                  v-model="sellingAmount"
                  label="Amount Sold"
                  :rules="[
                    v =>
                      (!isNaN(parseFloat(v)) && isFinite(v)) ||
                      'You have to type a number',
                    v =>
                      sellingVolumeNotHigherThanOwned(v) ||
                      'Can\'t sell more than you have !',
                  ]"
                ></v-text-field>
              </v-form>
            </v-col>
            <v-col cols="12">
              Predicted Cash Flow : {{ predictedCashFlowIfSell | toCurrency }}
            </v-col>
            <v-btn color="accent" class="mr-4" @click="validate">
              Vendre Crypto
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
  name: 'SellingModal',
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
      sellingAmount: 0,
      volume: 0,
      value: [],
      gradient: ['#617be2', '#ff6473'],
    }
  },
  created() {
    axios
      .get(`/me/wallet/${this.currency.id}`)
      .then(response => {
        this.volume = response.data.volume
      })
      .catch(e => {})
    this.getCurrencyRates()
  },
  computed: {
    predictedCashFlowIfSell: function() {
      return (
        this.user.profile.cash_flow +
        this.sellingAmount * this.currency.last_value
      )
    },
  },
  methods: {
    validate() {
      axios
        .post('/transactions', {
          currency: this.currency.id,
          quantity: this.sellingAmount,
          isSale: true,
        })
        .then(response => {
          this.dialog = false
          this.$emit('finished')
          this.sellingAmount = 0
          auth.checkAuth()
        })
        .catch(e => this.errors.push(e))
    },
    sellingVolumeNotHigherThanOwned(value) {
      return value <= this.volume
    },
    getCurrencyRates() {
      axios
        .get(`/currencies/${this.currency.id}/rates`, {
          params: { interval: 'hour', limit: 100 },
        })
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
