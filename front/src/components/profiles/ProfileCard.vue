<template>
  <v-card class="ml-2 pa-2">
    <v-list-item three-line>
      <v-list-item-content>
        <v-list-item-title class="headline mb-1">{{
          user.username
        }}</v-list-item-title>
        <v-list-item-subtitle>
          {{ user.joinDate }}
        </v-list-item-subtitle>
        <v-list-item-subtitle>
          Cash Flow :
          {{ user.cashFlow | toCurrency }}
        </v-list-item-subtitle>
      </v-list-item-content>
      <v-list-item-avatar tile size="80" color="teal">
        <span class="white--text headline">{{ user.username[0] }}</span>
      </v-list-item-avatar>
    </v-list-item>
  </v-card>
</template>

<script>
export default {
  name: 'ProfileCard',
  props: {
    user: Object,
  },
}
</script>

<style scoped></style>
