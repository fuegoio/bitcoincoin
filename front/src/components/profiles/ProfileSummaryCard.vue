<template>
  <v-card outlined class="ma-4" hover to="/profile">
    <v-list-item three-line>
      <v-list-item-content>
        <div class="overline mb-4">Compte</div>
        <v-list-item-title class="headline mb-1">
          {{ profile.username }}
        </v-list-item-title>
        <v-list-item-subtitle>
          Trader
        </v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar tile size="80" color="primary">
        <span class="white--text headline">{{ profile.username[0] }}</span>
      </v-list-item-avatar>
    </v-list-item>

    <v-card-actions class="py-0 mt-2">
      <v-col>
        Cash
      </v-col>
      <v-col class="text-right">
        {{ profile.cash_flow | toCurrency }}
      </v-col>
    </v-card-actions>
    <v-card-actions class="primary py-0">
      <v-col>
        Portfolio
      </v-col>
      <v-col class="text-right font-weight-bold">
        <v-icon v-if="walletTrend === true" class="pb-1" color="success"
          >mdi-menu-up</v-icon
        >
        <v-icon v-else-if="walletTrend === false" class="pb-1" color="error"
          >mdi-menu-down</v-icon
        >
        {{ profile.wallet_value | toCurrency }}
      </v-col>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator'
import { User } from '@/models/user'

@Component({})
export default class ProfileSummaryCard extends Vue {
  @Prop() profile: User
  walletTrend: boolean | null = null

  @Watch('profile.wallet_value')
  updateWalletValue(newValue: number, oldValue: number): void {
    this.walletTrend = newValue >= oldValue
    console.log('test')
  }
}
</script>

<style scoped></style>
