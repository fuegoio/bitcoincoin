<template>
  <v-card>
    <v-row>
      <v-col class="currency-trend px-6" cols="8">
        <v-sparkline
          :value="value"
          auto-draw
          :gradient="gradient"
          gradient-direction="right"
          line-width="0.7"
          height="160"
          padding="12"
          stroke-linecap="round"
          smooth
        ></v-sparkline>
      </v-col>
      <v-col cols="4" class="px-3">
        <v-card-title class="headline">{{ currency.name }}</v-card-title>
        <v-card-subtitle
          >User Cash Flow : {{ user.cash_flow | toCurrency }}</v-card-subtitle
        >
        <v-card-subtitle
          >Current Value :
          {{ currency.lastValue | toCurrency }}</v-card-subtitle
        >
        <BuyingForm v-if="action === 'buy'" :currency="currency" />
        <SellingForm v-else :currency="currency" />
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import BuyingForm from '@/components/transactions/BuyingForm'
import SellingForm from '@/components/transactions/SellingForm'
import auth from '@/modules/auth'
export default {
  name: 'TransactionCard',
  components: { SellingForm, BuyingForm },
  props: {
    currency: Object,
    action: String,
  },
  data: function() {
    return {
      value: [423, 446, 675, 510, 590, 610, 760],
      gradient: ['#617be2', '#ff6473'],
      user: auth.user.profile,
    }
  },
}
</script>

<style scoped></style>
