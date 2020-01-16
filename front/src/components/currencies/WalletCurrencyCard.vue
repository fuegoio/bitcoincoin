<template>
  <v-card class="ml-2 pa-2">
    <v-list-item three-line>
      <v-list-item-avatar>
        <img
          v-bind:src="
            'https://static.coincap.io/assets/icons/' +
              currency.symbol +
              '@2x.png'
          "
          v-bind:alt="currency.symbol"
        />
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title class="headline mb-1">
          {{ currency.name }}
        </v-list-item-title>
        <v-list-item-subtitle>
          Current Value : {{ currency.lastValue | toCurrency }}
        </v-list-item-subtitle>
        <v-list-item-subtitle>
          Quantity Owned : {{ currency.volume }}
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-card-actions>
      <TransactionButton :currency="currency" action="buy" />
      <TransactionButton :currency="currency" action="sell" />
    </v-card-actions>
  </v-card>
</template>

<script>
import TransactionButton from '@/components/transactions/TransactionButton'
export default {
  name: 'WalletCurrencyCard',
  components: { TransactionButton },
  props: {
    currency: Object,
  },
}
</script>

<style scoped></style>
