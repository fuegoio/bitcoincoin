<template>
  <v-row>
    <v-col
      v-for="currency in cryptoCurrencies"
      :key="currency.id"
      lg="4"
      md="6"
      sm="12"
    >
      <WalletCurrencyCard :currency="currency" />
    </v-col>
  </v-row>
</template>

<script>
import WalletCurrencyCard from '@/components/currencies/WalletCurrencyCard'
export default {
  name: 'WalletContainer',
  components: { WalletCurrencyCard },
  data: function() {
    return {
      cryptoCurrencies: [
        {
          name: 'Bitcoin',
          volume: 30,
          lastValue: 6780.82,
          symbol: 'btc',
        },
        {
          name: 'Ethereum',
          volume: 50,
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
      ],
    }
  },
}
</script>

<style scoped></style>
