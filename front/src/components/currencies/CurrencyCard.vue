<template>
  <v-card class="ml-2 pa-2 secondary" elevation="4">
    <v-list-item three-line>
      <v-list-item-content>
        <v-list-item-title class="headline mb-1">
          {{ crypto.name }}
        </v-list-item-title>
        <v-list-item-subtitle>
          Current Value : {{ crypto.currentValue }} $
        </v-list-item-subtitle>
        <v-list-item-subtitle>
          Quantity Owned : {{ crypto.number }}
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
