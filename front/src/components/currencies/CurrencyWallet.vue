<template>
  <v-card>
    <v-row class="px-3">
      <v-col cols="4" class="pl-6 pt-3 title">
        Porfolio
      </v-col>
      <v-col cols="4" class="pr-6 text-left currency-wallet-value">
        <span class="title font-weight-light ml-3">
          Possédé : {{ wallet.volume }}
        </span>
      </v-col>
      <v-col cols="4" class="pr-6 text-right currency-wallet-value">
        <span class="title font-weight-bold ml-3">
          {{ wallet.value | toCurrency }}
        </span>
      </v-col>
    </v-row>
  </v-card>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import { Wallet } from '@/models/wallet'

@Component({})
export default class CurrencyWallet extends Vue {
  @Prop() wallet: Wallet
}
</script>

<style lang="scss" scoped>
.currency-wallet-value {
  border-left: 1px solid #3e3f3e;
}
</style>
