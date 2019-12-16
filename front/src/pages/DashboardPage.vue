<template>
  <v-row class="fill-height ml-5 mt-4">
    <v-col cols="12" class="pa-0">
      <span class="display-1 font-weight-bold">Dashboard</span>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { namespace } from 'vuex-class'

import MoleculeRulesContainer from '@/containers/MoleculeRulesContainer.vue'
import MoleculeRulesNavContainer from '@/containers/MoleculeRulesNavContainer.vue'
import MoleculeRuleCreationContainer from '@/containers/MoleculeRuleCreationContainer.vue'

const rulesModule = namespace('rules')

@Component({
  components: {
    MoleculeRulesContainer,
    MoleculeRulesNavContainer,
    MoleculeRuleCreationContainer,
  },
})
export default class MoleculePage extends Vue {
  @rulesModule.State ruleCreation!: boolean
}
</script>

<style lang="scss" scoped></style>
