<template>
  <v-card
    class="pa-2"
    hover
    outlined
    :to="'/currencies/' + currencyWalletInfo.currency.id"
  >
    <v-list-item three-line>
      <v-list-item-avatar>
        <img
          :src="currencyWalletInfo.currency.icon"
          :alt="currencyWalletInfo.currency.icon"
        />
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title class="headline mb-1">
          {{ currencyWalletInfo.currency.name }}
        </v-list-item-title>
        <v-list-item-subtitle>
          Current Value :
          {{ currencyWalletInfo.currency.last_value | toCurrency }}
        </v-list-item-subtitle>
        <v-list-item-subtitle>
          Quantity Owned : {{ currencyWalletInfo.volume }}
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-card-actions>
      <TransactionButton :currency="currencyWalletInfo.currency" action="buy" />
      <TransactionButton
        :currency="currencyWalletInfo.currency"
        action="sell"
      />
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
    currencyWalletInfo: Object,
  },
}
</script>

<style scoped></style>
