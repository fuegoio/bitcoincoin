<template>
  <v-row>
    <v-col cols="6">
      <v-avatar tile size="80">
        <img
          :src="
            'https://static.coincap.io/assets/icons/' +
              currency.symbol +
              '@2x.png'
          "
          :alt="currency.symbol"
        />
      </v-avatar>
    </v-col>
    <v-col cols="6">
      <h1>{{ currency.name }}</h1>
    </v-col>
    <v-card-subtitle>
      User Cash Flow : {{ user.cash_flow | toCurrency }}
    </v-card-subtitle>
    <v-card-subtitle>
      Current Value : {{ currency.last_value | toCurrency }}
    </v-card-subtitle>
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
