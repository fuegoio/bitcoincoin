<template>
  <v-row>
    <v-col v-if="!loading" cols="12" class="pa-0 pl-4">
      <v-row>
        <v-col cols="5" class="pl-6 pt-3">
          <v-img
            :src="currency.icon"
            :alt="currency.symbol"
            class="currency-icon"
          />
          <span class="headline font-weight-bold">{{ currency.name }}</span>
          <div class="caption">
            {{ currency.symbol.toUpperCase() }}
          </div>
        </v-col>
        <v-col cols="3" class="pr-6 pt-5 text-right">
          <v-row justify="center" align="center">
            <v-icon large color="success">mdi-menu-up</v-icon>
            <span class="headline font-weight-light ml-3">
              {{ currency.last_value | toCurrency }}
            </span>
          </v-row>
        </v-col>
        <v-col cols="2" align-self="center">
          <TransactionButton :currency="currency" action="buy" />
        </v-col>
        <v-col cols="2" align-self="center">
          <TransactionButton :currency="currency" action="sell" />
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { Currency } from '@/models/currency'
import axios, { AxiosResponse } from 'axios'
import TransactionButton from '@/components/transactions/TransactionButton.vue'

@Component({
  components: { TransactionButton },
})
export default class CurrencyPage extends Vue {
  currency: Currency = null
  loading = true

  async fetchCurrency(): Promise<Currency> {
    const currencyId: number = parseInt(this.$route.params.currencyId)
    const response: AxiosResponse = await axios.get('/currencies/' + currencyId)
    return response.data
  }

  created() {
    this.fetchCurrency().then(currency => {
      this.currency = currency
      this.loading = false
    })
  }
}
</script>

<style lang="scss" scoped>
.currency-icon {
  width: 42px;
  margin-top: 6px;
  margin-right: 22px;
  float: left;
}
</style>
