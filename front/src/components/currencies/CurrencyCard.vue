<template>
  <v-card hover outlined :to="'/currencies/' + currency.id">
    <v-row class="px-3">
      <v-col cols="7" class="pl-6 pt-3 currency-card-name">
        <v-img
          :src="currency.icon"
          :alt="currency.symbol"
          class="currency-icon"
        />
        <span class="headline font-weight-bold">{{ currency.name }}</span>
        <div class="caption">
          {{ currency.symbol.toUpperCase() }}
        </div>
      </v-col>
      <v-col cols="5" class="pr-6 pt-5 text-right currency-card-value">
        <v-row justify="center" align="center">
          <v-icon large color="success">mdi-menu-up</v-icon>
          <span class="headline font-weight-light ml-3">
            {{ currency.last_value | toCurrency }}
          </span>
        </v-row>
      </v-col>
      <v-col cols="12" class="currency-trend px-6">
        <v-sparkline
          v-if="trend"
          :value="currency.last_rates"
          auto-draw
          :gradient="gradient"
          :labels="labels"
          label-size="6"
          gradient-direction="right"
          line-width="2"
          height="80"
          padding="12"
          stroke-linecap="round"
          smooth
        >
        </v-sparkline>
        <v-skeleton-loader v-else type="image" class="mx-auto">
        </v-skeleton-loader>
      </v-col>
    </v-row>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator'
import { Currency } from '@/models/currency'

@Component({})
export default class CurrencyCard extends Vue {
  @Prop() currency: Currency
  trend = false

  created() {
    let nullRates = false
    this.currency.last_rates.forEach((rate: number) => {
      if (rate === null) {
        nullRates = true
      }
    })
    this.trend = !nullRates
  }

  labels = ['4j', '3j', '2j', '1j', 'ce matin', '-']
  gradient = ['#617be2', '#ff6473']
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
