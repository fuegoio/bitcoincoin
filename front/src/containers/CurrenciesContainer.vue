<template>
  <v-row>
    <v-col v-for="currency in currencies" :key="currency.name" cols="6">
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
  ]
}
</script>

<style scoped></style>
