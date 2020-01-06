<template>
  <v-card class="ml-2 pa-2" elevation="4">
    <v-list-item three-line>
      <v-list-item-content>
        <v-list-item-title class="headline mb-1">
          {{ currency.name }}
        </v-list-item-title>
        <v-list-item-subtitle>
          Current Value : {{ currency.last_value }} $
        </v-list-item-subtitle>
        <v-list-item-subtitle>
          Quantity Owned : {{ currency.volume }}
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
  </v-card>
</template>

<script>
export default {
  name: 'CurrencyCard',
  props: {
    crypto: Object,
  },
}
</script>

<style scoped></style>
