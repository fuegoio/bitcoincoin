<template>
  <v-row>
    <v-col cols="12">
      <v-form class="px-3">
        <v-text-field
          v-model="sellingAmount"
          label="Amount Sold"
          :rules="[
            v =>
              sellingVolumeNotHigherThanOwned(v) ||
              'Can\'t sell more than you have !',
          ]"
        ></v-text-field>
      </v-form>
    </v-col>
    <v-col cols="4">
      Predicted Cash Flow
    </v-col>
    <v-col class="text-center" cols="8">
      {{ predictedCashFlowIfSell | toCurrency }}
    </v-col>
    <v-btn color="accent" class="mr-4" @click="validate">
      Sell Crypto
    </v-btn>
  </v-row>
</template>

<script>
import auth from '@/modules/auth'
import axios from 'axios'

export default {
  name: 'SellingForm',
  props: {
    currency: Object,
  },
  data: () => {
    return {
      sellingAmount: 0,
      user: auth.user.profile,
      volume: 0,
    }
  },
  created() {
    axios
      .get(`http://localhost:8000/api/v1/me/wallet/${this.currency.id}`)
      .then(response => {
        this.volume = response.data.volume
      })
      .catch(e => {})
  },
  computed: {
    predictedCashFlowIfSell: function() {
      return this.user.cash_flow + this.sellingAmount * this.currency.last_value
    },
  },
  methods: {
    validate() {
      axios
        .post('http://localhost:8000/api/v1/transactions', {
          user_id: this.user.id,
          currency_id: this.currency.id,
          quantity: this.sellingAmount,
          is_sale: true,
        })
        .then(response => {
          // Doit afficher que l'achat a bien été effectué
          // De même doit refresh
        })
        .catch(e => {})
    },
    sellingVolumeNotHigherThanOwned(value) {
      return value <= this.volume
    },
  },
}
</script>

<style scoped></style>
