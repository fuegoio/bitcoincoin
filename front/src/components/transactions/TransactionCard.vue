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
        <HeaderTransactionForm :currency="currency" />
        <BuyingForm v-if="action === 'buy'" :currency="currency" />
        <SellingForm v-else :currency="currency" />
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import BuyingForm from '@/components/transactions/BuyingForm'
import SellingForm from '@/components/transactions/SellingForm'
import HeaderTransactionForm from '@/components/transactions/HeaderTransactionForm'
import auth from '@/modules/auth'
export default {
  name: 'TransactionCard',
  components: { SellingForm, BuyingForm, HeaderTransactionForm },
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
