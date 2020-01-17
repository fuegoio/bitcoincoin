<template>
  <v-card class="ml-2 pa-2">
    <v-list-item three-line>
      <v-list-item-avatar>
        <img
          :src="
            'https://static.coincap.io/assets/icons/' +
              currencyAllData.symbol +
              '@2x.png'
          "
          :alt="currencyAllData.symbol"
        />
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title class="headline mb-1">
          {{ currencyAllData.name }}
        </v-list-item-title>
        <v-list-item-subtitle>
          Current Value : {{ currencyAllData.lastValue | toCurrency }}
        </v-list-item-subtitle>
        <v-list-item-subtitle>
          Quantity Owned : {{ currencyAllData.volume }}
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-card-actions>
      <TransactionButton :currency="currencyAllData" action="buy" />
      <TransactionButton :currency="currencyAllData" action="sell" />
    </v-card-actions>
  </v-card>
</template>

<script>
import TransactionButton from '@/components/transactions/TransactionButton'
import axios from 'axios'

export default {
  name: 'WalletCurrencyCard',
  components: { TransactionButton },
  props: {
    currencyInfo: Object,
  },
  data() {
    return {
      currencyAllData: {
        name: '',
        symbol: 'btc',
        lastValue: 0,
        volume: 0,
      },
    }
  },
  created() {
    axios
      .get(
        'http://localhost:8000/api/v1/currencies/' + this.currencyInfo.currency,
      )
      .then(
        response =>
          (this.currencyAllData = {
            name: response.data.name,
            symbol: response.data.symbol.toLowerCase(),
            lastValue: response.data.last_value,
            volume: this.currencyInfo.volume,
          }),
      )
  },
}
</script>

<style scoped></style>
