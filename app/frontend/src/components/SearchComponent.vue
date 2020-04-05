<template>
    <div id="search-wrapper" class="container">
        <div class="row">
            <div class="col-sm-10 offset-sm-1 text-center">
                <div class="input-group mb-3">
                    <input
                        v-model="query"
                        type="text"
                        class="form-control"
                        placeholder="Introduce Twitter Username/Bio"
                        aria-label="Introduce Twitter Username/Bio"
                        aria-describedby="button-addon2"
                    />
                    <div class="input-group-append">
                        <button
                            @click="getProfiles"
                            class="btn btn-outline-primary"
                            type="button"
                            id="button-addon2"
                        >
                            Search!
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <card :profiles="this.profiles"></card>
    </div>
</template>

<script>
import axios from 'axios';
import Card from './CardComponent';
export default {
    name: 'search',
    components: {
        Card,
    },
    data() {
        return {
            query: null,
            profiles: null,
        };
    },
    methods: {
        getProfiles() {
            const path = `http://localhost:5000/api/1.0/profiles/${this.query}`;
            axios
                .get(path)
                .then((res) => {
                    this.profiles = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
    },
};
</script>

<style>
#search-wrapper {
    margin-top: 50px;
}
</style>
