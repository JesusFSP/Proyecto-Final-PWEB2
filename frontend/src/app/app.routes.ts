import { Routes } from '@angular/router';

import { HomeComponent } from './pages/home/home';
import { ReservaListComponent } from './pages/reserva-list/reserva-list';
import { ReservaFormComponent } from './pages/reserva-form/reserva-form';

export const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'reservas', component: ReservaListComponent },
  { path: 'reservas/crear', component: ReservaFormComponent },
  { path: 'reservas/editar/:id', component: ReservaFormComponent },
];