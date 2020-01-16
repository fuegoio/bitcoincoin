<template>
  <v-row justify="center">
    <v-btn
      v-if="action === 'buy'"
      color="success"
      dark
      @click.stop="dialog = true"
    >
      Acheter
    </v-btn>
    <v-btn v-else color="accent" dark @click.stop="dialog = true">
      Vendre
    </v-btn>
    <v-dialog v-model="dialog" transition="slide-x-reverse-transition">
      <TransactionCard
        :currencyWalletInfo="currencyWalletInfo"
        :action="action"
      />
    </v-dialog>
  </v-row>
</template>
<script>
import TransactionCard from '@/components/transactions/TransactionCard'
export default {
  name: 'TransactionButton',
  components: { TransactionCard },
  props: {
    currencyWalletInfo: Object,
    action: String,
  },
  data: function() {
    return {
      dialog: false,
    }
  },
}
</script>

<style scoped>
.currency-icon {
  width: 42px;
  margin-top: 6px;
  margin-right: 22px;
  float: left;
}

.currency-card-name,
.currency-card-value {
  border-bottom: 1px solid #3e3f3e;
}

.currency-card-value {
  border-left: 1px solid #3e3f3e;
}
</style>
