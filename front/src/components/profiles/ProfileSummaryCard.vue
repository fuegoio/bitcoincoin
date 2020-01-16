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

    <v-row class="py-0 mt-2 px-2 mx-0">
      <v-col cols="4">
        Cash
      </v-col>
      <v-col class="text-right" cols="8">
        {{ profile.cash_flow | toCurrency }}
      </v-col>
      <v-col cols="4">
        Porfolio
      </v-col>
      <v-col class="text-right" cols="8">
        {{ profile.wallet_value | toCurrency }}
      </v-col>
    </v-row>
    <v-row class="py-0 px-2 mx-0 primary">
      <v-col cols="4">
        Total
      </v-col>
      <v-col class="text-right font-weight-bold" cols="8">
        <v-icon v-if="valueTrend === true" class="pb-1" color="success">
          mdi-menu-up
        </v-icon>
        <v-icon v-else-if="valueTrend === false" class="pb-1" color="error">
          mdi-menu-down
        </v-icon>
        {{ profile.value | toCurrency }}
      </v-col>
    </v-row>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator'
import { User } from '@/models/user'

@Component({})
export default class ProfileSummaryCard extends Vue {
  @Prop() profile: User
  valueTrend: boolean | null = null

  @Watch('profile.value')
  updateValue(newValue: number, oldValue: number): void {
    this.valueTrend = newValue >= oldValue
  }
}
</script>

<style scoped></style>
