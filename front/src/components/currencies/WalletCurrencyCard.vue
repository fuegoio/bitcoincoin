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
          Current Value : {{ currency.lastValue }} $
        </v-list-item-subtitle>
        <v-list-item-subtitle>
          Quantity Owned : {{ currency.volume }}
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-card-actions>
      <BuyingButton :currency="currency"></BuyingButton>
    </v-card-actions>
  </v-card>
</template>

<script>
import BuyingButton from '@/components/transactions/BuyingButton'
export default {
  name: 'CurrencyCard',
  components: { BuyingButton },
  props: {
    currency: Object,
  },
}
</script>

<style scoped></style>
