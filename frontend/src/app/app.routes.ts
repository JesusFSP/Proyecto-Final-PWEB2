import { Routes } from '@angular/router';
import { ReservaListComponent } from './pages/reserva-list';
import { ReservaFormComponent } from './pages/reserva-form';

export const routes: Routes = [
  { path: '', component: ReservaListComponent },
  { path: 'nueva', component: ReservaFormComponent },
  { path: '**', redirectTo: '' },
];