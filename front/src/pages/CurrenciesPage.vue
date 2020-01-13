<template>
  <v-row class="pt-4">
    <v-col cols="12" class="pa-0 pl-3">
      <span class="display-1 font-weight-bold">Currencies</span>
    </v-col>
    <v-col cols="12" class="mt-4">
      <CurrenciesContainer />
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import CurrenciesContainer from '@/containers/CurrenciesContainer.vue'

@Component({
  components: {
    CurrenciesContainer,
  },
})
export default class CurrenciesPage extends Vue {}
</script>

<style lang="scss" scoped></style>
