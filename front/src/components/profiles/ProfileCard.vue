<template>
  <v-card class="py-3" outlined>
    <v-list-item three-line>
      <v-list-item-content>
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
  </v-card>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import { User } from '@/models/user'

@Component({})
export default class ProfileCard extends Vue {
  @Prop() profile: User
}
</script>

<style scoped></style>
