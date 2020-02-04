<template>
  <v-row>
    <v-col v-if="!loading && !member" cols="12">
      <v-banner single-line>
        Vous ne faites pas partie de cette banque, vous pouvez demander à la
        rejoindre.
        <template v-slot:actions>
          <v-btn
            v-if="!joinDemandAsked"
            text
            color="primary"
            @click="askToJoinBank"
            >Demander à rejoindre</v-btn
          >
          <v-btn v-else text disabled>Demande envoyée</v-btn>
        </template>
      </v-banner>
    </v-col>
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
      <v-card
        v-if="bank.demands && bank.demands.length > 0"
        outlined
        class="my-6"
      >
        <v-card-title>
          Demandes
        </v-card-title>
        <v-data-table
          :headers="demandHeaders"
          :items="bank.demands"
          hide-default-footer
        >
          <template v-slot:item.name="{ item }">
            <v-row align="center">
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
          <template v-slot:item.approval="{ item }">
            <v-row>
              <v-edit-dialog @save="approve(item.user.id, item.rank)">
                <v-btn icon>
                  <v-icon small color="success">
                    mdi-check
                  </v-icon>
                </v-btn>
                <template v-slot:input>
                  <v-select
                    v-model="item.rank"
                    :items="['Admin', 'Trader']"
                    label="Rank"
                    single-line
                  ></v-select>
                </template>
              </v-edit-dialog>
              <v-btn icon @click="disapprove(item.user.id)">
                <v-icon small color="error">
                  mdi-cancel
                </v-icon>
              </v-btn>
            </v-row>
          </template>
        </v-data-table>
      </v-card>
    </v-col>
    <v-col v-if="!loading" cols="12">
      <v-card>
        <v-card-title>
          Membres
        </v-card-title>
        <v-data-table
          :headers="memberHeaders"
          :items="bank.memberships"
          hide-default-footer
        >
          <template v-slot:item.name="{ item }">
            <v-row align="center">
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
import auth from '../modules/auth'

@Component({})
export default class BankPage extends Vue {
  user = auth.user.profile
  bank: Bank = null
  loading = true
  demandHeaders = [
    { text: 'Nom', value: 'name' },
    { text: 'Cash', value: 'cash_flow' },
    { text: 'Porfolio', value: 'wallet_value' },
    { text: 'Total', value: 'value' },
    { text: 'Approbation', value: 'approval' },
  ]
  memberHeaders = [
    { text: 'Nom', value: 'name' },
    { text: 'Rang', value: 'rank' },
    { text: 'Cash', value: 'cash_flow' },
    { text: 'Porfolio', value: 'wallet_value' },
    { text: 'Total', value: 'value' },
  ]
  member = false
  joinDemandAsked = false

  async fetchBank(): Promise<Bank> {
    const bankId: number = parseInt(this.$route.params.bankId)
    const response: AxiosResponse = await axios.get('/banks/' + bankId)
    return response.data
  }

  async askToJoinBank(): Promise<Bank> {
    const bankId: number = parseInt(this.$route.params.bankId)
    const response: AxiosResponse = await axios.post('/banks/' + bankId)
    this.joinDemandAsked = true
    return response.data
  }

  async approve(userId: number, rank: string): Promise<void> {
    const bankId: number = parseInt(this.$route.params.bankId)
    const response: AxiosResponse = await axios.post(
      '/banks/' + bankId + '/members',
      {
        userId: userId,
        rank: rank,
      },
    )
    this.bank = response.data
  }

  async disapprove(userId: number): Promise<void> {
    const bankId: number = parseInt(this.$route.params.bankId)
    const response: AxiosResponse = await axios.post(
      '/banks/' + bankId + '/members',
      {
        userId: userId,
      },
    )
    this.bank = response.data
  }

  created() {
    this.fetchBank().then(bank => {
      this.bank = bank
      this.bank.memberships.forEach(m => {
        if (m.user.id === this.user.id) {
          this.member = true
        }
      })
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
