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
      <BuyingModal :currency="currencyWalletInfo.currency" />
      <SellingModal :currency="currencyWalletInfo.currency" />
    </v-card-actions>
  </v-card>
</template>

<script>
import BuyingModal from '@/components/transactions/BuyingModal'
import SellingModal from '@/components/transactions/SellingModal'

export default {
  name: 'WalletCurrencyCard',
  components: { SellingModal, BuyingModal },
  props: {
    currencyWalletInfo: Object,
  },
}
</script>

<style scoped></style>
