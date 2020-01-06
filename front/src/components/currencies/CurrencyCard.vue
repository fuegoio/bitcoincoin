<template>
  <v-card hover shaped>
    <v-row>
      <v-col cols="8" class="pl-10 currency-card-name">
        <img :src="image" :alt="currency.symbol" class="currency-icon" />
        <span class="display-1 font-weight-bold">{{ currency.name }}</span>
      </v-col>
      <v-col cols="4" class="text-right pr-10 currency-card-value">
        <v-row justify="center" align="center">
          <v-icon large color="success">mdi-menu-up</v-icon>
          <span class="display-1 font-weight-light ml-3">
            $ {{ currency.lastValue }}
          </span>
        </v-row>
      </v-col>
      <v-col cols="12" class="currency-trend px-6">
        <v-sparkline
          :value="value"
          auto-draw
          :gradient="gradient"
          gradient-direction="right"
          line-width="0.7"
          height="80"
          padding="12"
          stroke-linecap="round"
          smooth
        >
        </v-sparkline>
      </v-col>
    </v-row>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator'

@Component({})
export default class CurrencyCard extends Vue {
  @Prop() currency: any
  image =
    'https://static.coincap.io/assets/icons/' + this.currency.symbol + '@2x.png'

  value = [423, 446, 675, 510, 590, 610, 760]
  gradient = ['#617be2', '#ff6473']
}
</script>

<style scoped>
.currency-icon {
  width: 40px;
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
