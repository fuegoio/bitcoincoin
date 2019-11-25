<template>
  <v-row class="flex-column pl-12 pt-5 nav">
    <v-col>
      <div class="overline">
        Analgésiques > Paracétamol
      </div>
      <div class="display-2 font-weight-black mt-5">
        Paracétamol
      </div>
      <div class="caption mt-3">
        Douleur légère, Douleur modérée, Fièvre
      </div>
    </v-col>
    <v-col>
      <v-scroll-x-transition mode="out-in">
        <v-btn
          v-if="!ruleCreation"
          block
          color="primary"
          @click="toggleRuleCreation"
        >
          <v-icon left>mdi-plus</v-icon>
          Ajouter une règle
        </v-btn>
        <v-btn v-else block color="grey" @click="toggleRuleCreation">
          <v-icon left>mdi-arrow-left</v-icon>
          Revenir aux règles
        </v-btn>
      </v-scroll-x-transition>
    </v-col>
    <v-col class="mt-2">
      <span class="font-weight-bold">5</span> règles ajoutées
      <v-divider class="mt-2"></v-divider>
      <v-list nav dense :disabled="ruleCreation">
        <v-list-item-group
          color="primary"
          :value="ruleTypeScroll"
          @change="updateRuleTypeScroll"
        >
          <v-list-item v-for="(rule, i) in ruleTypes" :key="i">
            <v-list-item-content>
              <v-list-item-title>
                {{ rule.value }}
                <span v-if="rule.count" class="grey--text caption"
                  >({{ rule.count }})</span
                >
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-col>
    <v-col class="mt-2">
      <span class="text--darken-3 grey--text">Autres analgésiques</span>
      <v-divider class="mt-2"></v-divider>
      <div class="ml-2 mt-3">
        <div class="grey--text">Morphine</div>
        <div class="grey--text">Opium</div>
        <div class="grey--text">Oxycodone</div>
        <div class="grey--text">Codéine</div>
        <div class="grey--text">Pentazocine</div>
        <div class="grey--text">Acide acétylsalicylique</div>
      </div>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import { namespace } from 'vuex-class'
import { Count } from '@/types/types'

const rulesModule = namespace('rules')

@Component({})
export default class MoleculeRulesNavContainer extends Vue {
  @rulesModule.Getter('ruleTypesWithCounts') ruleTypes!: Count<string>[]

  @rulesModule.State ruleTypeScroll!: number
  @rulesModule.Mutation('updateRuleTypeScrollFromNav') updateRuleTypeScroll!: {}

  @rulesModule.State ruleCreation!: boolean
  @rulesModule.Mutation toggleRuleCreation!: () => void
}
</script>

<style lang="scss" scoped>
.nav {
  position: fixed;
  margin: auto;
}
</style>
