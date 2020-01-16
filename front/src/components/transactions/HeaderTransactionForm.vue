<template>
  <v-row>
    <v-col cols="6">
      <v-img
        :src="currency.icon"
        :alt="currency.symbol"
        height="80"
        width="80"
      />
    </v-col>
    <v-col cols="6">
      <h1>{{ currency.name }}</h1>
    </v-col>
    <v-col cols="4">
      Cash
    </v-col>
    <v-col class="text-center" cols="8">
      {{ user.cash_flow | toCurrency }}
    </v-col>
    <v-col cols="4"> Current Value {{ currency.name }} </v-col>
    <v-col class="text-center" cols="8">
      {{ currency.last_value | toCurrency }}
    </v-col>
  </v-row>
</template>

<script>
import auth from '@/modules/auth'
export default {
  name: 'HeaderTransactionForm',
  props: {
    currency: Object,
  },
  data() {
    return {
      user: auth.user.profile,
    }
  },
}
</script>

<style scoped></style>
