<template>
  <v-card outlined>
    <v-card-title>
      Transactions
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="transactions"
      :items-per-page="10"
      class="elevation-1"
    >
      <template v-slot:item.currency="{ item }">
        <v-row align="center">
          <v-list-item-avatar size="24">
            <v-img :src="item.currency.icon" :alt="item.currency.symbol" />
          </v-list-item-avatar>
          <span class="font-weight-bold body-1">
            {{ item.currency.name }}
          </span>
        </v-row>
      </template>
      <template v-slot:item.type="{ item }">
        <v-chip v-if="item.is_sale" color="error" dark>Vente</v-chip>
        <v-chip v-else color="success" dark>Achat</v-chip>
      </template>
      <template v-slot:item.value="{ item }">
        {{ item.value | toCurrency }}
      </template>
    </v-data-table>
  </v-card>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import { Transaction } from '@/models/transaction'

@Component({})
export default class CurrencyTransactions extends Vue {
  @Prop() transactions: Transaction[]
  headers = [
    { text: 'Monnaie', value: 'currency' },
    { text: 'Type', value: 'type' },
    { text: 'Quantitée', value: 'quantity' },
    { text: 'Valeur', value: 'value' },
    { text: 'Date', value: 'datetime.diff' },
  ]
}
</script>

<style lang="scss" scoped>
.money-graph {
  min-height: 500px;
}
</style>
