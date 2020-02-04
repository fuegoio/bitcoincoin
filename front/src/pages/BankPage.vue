<template>
  <v-row>
    <v-col v-if="!loading" cols="12" class="px-4">
      <v-row>
        <v-col cols="3" class="pl-6 pt-3">
          <span class="headline font-weight-bold">{{ bank.name }}</span>
          <div class="caption">
            {{ bank.symbol.toUpperCase() }}
          </div>
        </v-col>
        <v-col cols="3" class="pr-6 pt-5 text-right">
          <span class="headline font-weight-light ml-3">
            {{ bank.cash_flow | toCurrency }}
          </span>
          <div class="caption">
            Cash
          </div>
        </v-col>
        <v-col cols="3" class="pr-6 pt-5 text-right">
          <span class="headline font-weight-light ml-3">
            {{ bank.wallet_value | toCurrency }}
          </span>
          <div class="caption">
            Porfolio
          </div>
        </v-col>
        <v-col cols="3" class="pr-6 pt-5 text-right">
          <span class="headline font-weight-bold ml-3">
            {{ bank.value | toCurrency }}
          </span>
          <div class="caption">
            Total
          </div>
        </v-col>
      </v-row>
    </v-col>
    <v-col v-if="!loading" cols="12">
      <v-card>
        <v-card-title>
          Membres
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="bank.memberships"
          hide-default-footer
        >
          <template v-slot:item.name="{ item }">
            <v-row align="center" @click="$router.push('/profile/' + item.id)">
              <v-list-item-avatar tile size="18" color="primary">
                <span class="white--text">{{ item.user.username[0] }}</span>
              </v-list-item-avatar>
              <span class="font-weight-bold">
                {{ item.user.username }}
              </span>
            </v-row>
          </template>
          <template v-slot:item.cash_flow="{ item }">
            <span>{{ item.user.cash_flow | toCurrency }}</span>
          </template>
          <template v-slot:item.wallet_value="{ item }">
            <span>{{ item.user.wallet_value | toCurrency }}</span>
          </template>
          <template v-slot:item.value="{ item }">
            <span>{{ item.user.value | toCurrency }}</span>
          </template>
        </v-data-table>
      </v-card>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import axios, { AxiosResponse } from 'axios'

import { Bank } from '@/models/bank'

@Component({})
export default class BankPage extends Vue {
  bank: Bank = null
  loading = true
  headers = [
    { text: 'Nom', value: 'name' },
    { text: 'Rang', value: 'rank' },
    { text: 'Cash', value: 'cash_flow' },
    { text: 'Porfolio', value: 'wallet_value' },
    { text: 'Total', value: 'value' },
  ]

  async fetchBank(): Promise<Bank> {
    const bankId: number = parseInt(this.$route.params.bankId)
    const response: AxiosResponse = await axios.get('/banks/' + bankId)
    return response.data
  }

  created() {
    this.fetchBank().then(bank => {
      this.bank = bank
      this.loading = false
    })
  }
}
</script>

<style lang="scss" scoped>
.currency-icon {
  width: 42px;
  margin-top: 6px;
  margin-right: 22px;
  float: left;
}
</style>
