import { Routes } from '@angular/router';
import { ReservaListComponent } from './pages/reserva-list';
import { ReservaFormComponent } from './pages/reserva-form';
import { HomeComponent } from './pages/home/home.component';

export const routes: Routes = [
  { path: '', component: ReservaListComponent },
  { path: 'nueva', component: ReservaFormComponent },
  { path: '**', redirectTo: '' },
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', loadChildren: () => import('./pages/home/home').then(m => m.Home) },
];