<template>
  <v-row>
    <v-col v-for="currency in currencies" :key="currency.name" cols="4">
      <CurrencyCard :currency="currency" />
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import CurrencyCard from '@/components/currencies/CurrencyCard.vue'

@Component({
  components: {
    CurrencyCard,
  },
})
export default class CurrenciesContainer extends Vue {
  currencies = [
    {
      name: 'Bitcoin',
      lastValue: 6780.82,
      symbol: 'btc',
    },
    {
      name: 'Ethereum',
      lastValue: 135.19,
      symbol: 'eth',
    },
    {
      name: 'Cosmos',
      volume: 100,
      lastValue: 150,
      symbol: 'atom',
    },
    {
      name: 'Bitcoin Cash',
      volume: 200,
      lastValue: 190.86,
      symbol: 'bch',
    },
    {
      name: 'Litecoin',
      volume: 100,
      lastValue: 40.68,
      symbol: 'ltc',
    },
    {
      name: 'XRP',
      volume: 100,
      lastValue: 0.21,
      symbol: 'xrp',
    },
  ]
}
</script>

<style scoped></style>
