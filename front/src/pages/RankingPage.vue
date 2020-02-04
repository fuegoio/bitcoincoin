<template>
  <v-card>
    <v-card-title>
      Classement
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table :headers="headers" :items="users" :search="search">
      <template v-slot:item.username="{ item }">
        <v-row align="center">
          <v-list-item-avatar tile size="18" color="primary">
            <span class="white--text">{{ item.username[0] }}</span>
          </v-list-item-avatar>
          <span class="font-weight-bold">
            {{ item.username }}
          </span>
        </v-row>
      </template>
      <template v-slot:item.cash_flow="{ item }">
        <span>{{ item.cash_flow | toCurrency }}</span>
      </template>
      <template v-slot:item.wallet_value="{ item }">
        <span>{{ item.wallet_value | toCurrency }}</span>
      </template>
      <template v-slot:item.value="{ item }">
        <span>{{ item.value | toCurrency }}</span>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import axios from 'axios'
export default {
  name: 'RankingPage',
  data: function() {
    return {
      search: '',
      headers: [
        { text: 'Rank', value: 'ranking' },
        { text: 'Username', value: 'username' },
        { text: 'Cash Flow', value: 'cash_flow' },
        { text: 'Wallet Value', value: 'wallet_value' },
        { text: 'Total Value', value: 'value' },
      ],
      users: [],
    }
  },
  created() {
    axios.get('http://localhost:8000/api/v1/users').then(response => {
      const listUsers = []
      for (const [index, user] of response.data.entries()) {
        listUsers.push({
          ranking: index + 1,
          username: user.username,
          cash_flow: user.cash_flow,
          wallet_value: user.wallet_value,
          value: user.value,
        })
      }
      this.users = listUsers
    })
  },
}
</script>

<style scoped></style>
